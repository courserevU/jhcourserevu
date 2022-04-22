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

      <br />
      <!-- Search Dropdown to filter within reviews-->
      <div class="flex flex-row space-x-3">
        <SelectReviewMenu :options="filters" @update-option="updateOption" />
      </div>

      <div
        class="mt-6 grid grid-cols-1"
        :class="[isTile ? 'gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8' : '']"
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
        <Pagination
          @change-page="changePage"
          :maxPage="totalPages"
          :pageReplacement="page"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Search from "./Search.vue";
import SelectReviewMenu from "./SelectReviewMenu.vue";
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
      mod: true, // true if current user is moderator - will come from API
      isTile: true,
      totalPages: 5,
      reviewCount: 1,
      option: 1,
      filters: [
        {
          id: 2,
          name: "Teaching Style",
        },
        {
          id: 3,
          name: "Grading Style",
        },
        {
          id: 4,
          name: "Teacher Feedback",
        },
        {
          id: 5,
          name: "Workload",
        },
        {
          id: 6,
          name: "Assignment Style",
        },
        {
          id: 7,
          name: "Exam Style",
        },
      ],
    };
  },
  props: {
    course: String, // passed as stringified Object, needs to be parsed
  },
  components: { Search, Pagination, SelectReviewMenu, AnnotationIcon, XIcon },
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
        this.reviewCount = data.count;
        this.totalPages = Math.ceil(this.reviewCount / 10);
      });
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
    toggleLayout() {
      this.isTile = !this.isTile;
    },
    deleteReview(id: number) {
      axios
        .delete(
          `https://jhcourserevu-api-test.herokuapp.com/course/review/api/${id}/`
        )
        .then(() => {
          // Reload page with updated review list (same page unless deletion reduces # of pages)
          if (this.page === this.totalPages && this.reviewCount % 10 === 1) {
            this.page -= 1;
          }
          axios
            .get(
              `https://jhcourserevu-api-test.herokuapp.com/course/review/api/${
                JSON.parse(this.course).id
              }/?page=${this.page}`
            )
            .then((response) => {
              const data = response.data;
              this.reviews = data.results;
              this.reviewCount = data.count;
              this.totalPages = Math.ceil(this.reviewCount / 10);
            });
        });
    },
    updateOption(e: any) {
      if (e === undefined) return;
      this.option = e.id;
    },
  },
});
</script>
