<template>
  <div class="bg-white dark:bg-gray-800">
    <div
      class="max-w-2xl mx-auto py-16 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8"
    >
      <h2
        class="text-2xl font-extrabold tracking-tight text-gray-900 dark:text-gray-200"
      >
        Reviews for {{ course }}
      </h2>

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
                <a> Professor: {{ review.professor }} </a>
              </h3>
              <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                {{ review.review }}
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
    professor: "Ali Madooei",
    review: "Greatest teaching ever!",
    page: 1,
  },
  {
    id: 2,
    professor: "Imaginary Professor",
    review: "Entirely self-directed class - the professor never appeared!",
    page: 1,
  },
  {
    id: 3,
    professor: "Mr. Anderson",
    review: "We live in a simulation.",
    page: 1,
  },
  {
    id: 4,
    professor: "Mr. Smith",
    review: "*equip sunglasses*",
    page: 1,
  },
  {
    id: 5,
    professor: "[REDACTED]",
    review: "Alllll byyy MYYYYYSELLLLF!",
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
    course: String,
  },
  methods: {
    changePage(e: number) {
      this.page = e;
    },
    goToWriteReview(course: any) {
      this.$router.push({
        path: "/write",
        name: "write",
        params: { course: course },
      });
    },
    goToReadReviews(course: any) {
      this.$router.push({ name: "read", params: { course: course } });
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
    // Retrieves reviews for given course to be displayed by the component
    /*axios
      .get(`https://jhcourserevu-api.herokuapp.com/course/review/api/${course.id}}`)
      .then((response) => {
        this.reviews = response.data;
      });
    */
  },
});
</script>
