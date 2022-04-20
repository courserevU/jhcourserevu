<template>
  <div class="bg-white dark:bg-gray-800">
    <div
      class="max-w-2xl mx-auto py-16 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8"
    >
      <h2
        class="text-2xl font-extrabold tracking-tight text-gray-900 dark:text-gray-200"
      >
        Reviews for {{ JSON.parse(course).name }}
      </h2>

      <!-- Search Bar for Reviews + Dropdown for more specific search -->
      <div class ="flex flex-row space-x-3">
        <Search @update-filter="updateFilter" />
        <SelectMenu :options=filters @update-option="updateOption" />
        <span
          class="input-group-text items-center px-3 py-3 text-base font-normal text-gray-700 dark:text-gray-200 text-center whitespace-nowrap rounded"
          id="basic-addon2"
        >
          <svg
            aria-hidden="true"
            focusable="false"
            data-prefix="fas"
            data-icon="search"
            class="w-4"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
          >
            <path
              fill="currentColor"
              d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"
            />
          </svg>
        </span>
      </div>

      <div
        class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8"
      >
        <div
          v-for="review in reviews"
          :key="reviews.indexOf(review)"
          class="group relative py-2 px-3 shadow-md dark:ring-gray-400 dark:ring-1 dark:rounded"
        >
          <div class="mt-2">
            <div class="relative">
              <div v-for="comment in review" :key="comment.id">
                <h3
                  class="text-md text-gray-700 dark:text-gray-300"
                  v-if="comment.category === 'Professor'"
                >
                  <span class="font-bold"> Professor: </span>
                  <span>{{ comment.comment }}</span>
                </h3>
                <p class="mt-2 text-sm text-gray-500 dark:text-gray-400" v-else>
                  <span class="font-bold">{{ comment.category }}: </span>
                  <span>{{ comment.comment }}</span>
                </p>
              </div>
              <!-- Below buttons only appear if user is moderator (not implemented) -->
              <div class="mt-4 relative float-right" v-if="mod">
                <button class="mr-3">
                  <!-- Send warning message to user who wrote given review -->
                  <AnnotationIcon
                    class="h-5 w-5 text-black dark:text-gray-200"
                  />
                </button>
                <!-- Delete given review -->
                <button @click="deleteReview(review[0].review)">
                  <XIcon class="h-5 w-5 text-red-600" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <Pagination @change-page="changePage" :maxPage="totalPages" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Search from "./Search.vue";
import Pagination from "./Pagination.vue";
import { AnnotationIcon, XIcon } from "@heroicons/vue/outline";

import axios from "axios";

let query = "";

export default defineComponent({
  name: "ReviewDisplay",
  data() {
    return {
      query,
      reviews: [],
      page: 1,
      totalPages: 0,
      mod: true, // true if current user is moderator - will come from API
    };
  },
  components: { Search, Pagination, AnnotationIcon, XIcon },
  props: {
    course: String, // passed as stringified Object, needs to be parsed
  },
  methods: {
    changePage(e: number) {
      this.page = e;

      axios
        .get(
          `https://jhcourserevu-api-test.herokuapp.com/course/review/api/${
            JSON.parse(this.course).id
          }/?page=${this.page}`
        )
        .then((response) => {
          const data = response.data;
          this.reviews = data.results;
        });
    },
    deleteReview(id: number) {
      axios
        .delete(
          `https://jhcourserevu-api-test.herokuapp.com/course/review/api/${id}/`
        )
        .then(() => {
          // Reload page with updated review list
          axios
            .get(
              `https://jhcourserevu-api-test.herokuapp.com/course/review/api/${
                JSON.parse(this.course).id
              }/`
            )
            .then((response) => {
              const data = response.data;
              this.reviews = data.results;
              this.totalPages = Math.ceil(data.count / 10);
            });
        });
    },
  },
  mounted() {
    // Retrieves reviews for the given course from the DB through the API, to display
    axios
      .get(
        `https://jhcourserevu-api-test.herokuapp.com/course/review/api/${
          JSON.parse(this.course).id
        }/`
      )
      .then((response) => {
        const data = response.data;
        this.reviews = data.results;
        this.totalPages = Math.ceil(data.count / 10);
      });
  },
});
</script>
