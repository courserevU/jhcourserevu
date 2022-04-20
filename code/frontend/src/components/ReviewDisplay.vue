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
          v-for="review in filteredReviews"
          :key="review.id"
          class="group relative py-2 px-3 shadow-md dark:ring-gray-400 dark:ring-1 dark:rounded"
        >
          <div class="mt-2">
            <div class="relative">
              <h3 class="text-md text-gray-700 dark:text-gray-300">
                <a> Professor: {{ review.comments[0] }} </a>
              </h3>
              <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                {{ review.comments.slice(1) }}
              </p>
              <!-- Below buttons only appear if user is moderator (not implemented) -->
              <div class="mt-4 relative float-right" v-if="mod">
                <button class="mr-3">
                  <!-- Send warning message to user who wrote given review -->
                  <AnnotationIcon
                    class="h-5 w-5 text-black dark:text-gray-200"
                  />
                </button>
                <!-- Delete given review -->
                <button class="">
                  <XIcon class="h-5 w-5 text-red-600" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <Pagination @change-page="changePage" />
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

// Pull reviews for a specific course from the DB with a GET request

let reviews = [
  {
    id: 1,
    comments: ["Prof Madooei", "Greatest teaching ever!"],
    page: 1,
  },
  {
    id: 2,
    comments: ["Imaginary Professor", "Entirely self-directed class - the professor never appeared!"],
    page: 1,
  },
  {
    id: 3,
    comments: ["Mr. Anderson", "We live in a simulation."],
    page: 1,
  },
  {
    id: 4,
    comments: ["Mr. Smith", "*equip sunglasses*"],
    page: 1,
  },
  {
    id: 5,
    comments: ["[REDACTED]", "Alllll byyy MYYYYYSELLLLF!"],
    page: 2,
  },

  // More reviews... load from our db
];

let query = "";

export default defineComponent({
  name: "ReviewDisplay",
  data() {
    return {
      query,
      reviews,
      page: 1,
      mod: false, // true if current user is moderator - will come from API
    };
  },
  components: { Search, Pagination, AnnotationIcon, XIcon },
  props: {
    course: String, // passed as stringified Object, needs to be parsed
  },
  methods: {
    changePage(e: number) {
      this.page = e;
    },
  },
  computed: {
    filteredReviews() {
      return this.reviews.filter((review: any) => {
        return review.page === this.page;
      });
    },
  },
  mounted() {
    // Retrieves reviews for the given course from the DB through the API, to display
    axios
      .get(`https://jhcourserevu-api.herokuapp.com/course/review/api/${JSON.parse(this.course).id}`) // page query?
      .then((response) => {
        this.reviews = response.data;
      });
  },
});
</script>
