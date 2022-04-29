<template>
  <div class="bg-white dark:bg-gray-800">
    <div
      class="max-w-2xl mx-auto py-16 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8"
    >
      <h2
        class="text-2xl font-extrabold tracking-tight text-gray-900 dark:text-gray-200"
      >
        {{ JSON.parse(course).name }} ({{ JSON.parse(course).course_num }})
      </h2>

      <h3 class="text-md text-gray-700 dark:text-gray-300">
        Prerequisites: {{ JSON.parse(course).prerequisites }}
      </h3>
      <h3 class="text-md text-gray-700 dark:text-gray-300">
        Corequisites: {{ JSON.parse(course).corequisites }}
      </h3>
      <h3 class="text-md text-gray-700 dark:text-gray-300">
        Credits: {{ JSON.parse(course).num_credits }}
      </h3>
      <h3 class="text-md text-gray-700 dark:text-gray-300">
        Section: {{ JSON.parse(course).meeting_section }}
      </h3>
      <h3 class="text-md text-gray-700 dark:text-gray-300">
        Department: {{ JSON.parse(course).department }}
      </h3>
      <h3 class="text-md text-gray-700 dark:text-gray-300">
        Campus: {{ JSON.parse(course).campus }}
      </h3>
      <h3 class="text-md text-gray-700 dark:text-gray-300">
        Writing Intensive:
        {{ JSON.parse(course).is_writing_intensive === "True" ? "Yes" : "No" }}
      </h3>
      <br />

      <!-- Search Dropdown to filter within reviews-->
      <div class="flex flex-row space-x-3">
        <SelectReviewMenu :options="filters" @update-option="updateOption" />
        <button
          class="ml-8 whitespace-nowrap h-11 items-center justify-center px-4 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-gray-200 hover:bg-slate-900 dark:bg-slate-900 dark:hover:bg-gray-100"
          @click="toggleLayout"
        >
          <ViewGridIcon
            :class="[
              open ? 'text-gray-600' : 'text-gray-400',
              'h-5 w-5 group-hover:text-gray-500',
            ]"
            v-if="isTile"
            aria-hidden="true"
          />
          <ViewListIcon
            :class="[
              open ? 'text-gray-600' : 'text-gray-400',
              'h-5 w-5 group-hover:text-gray-500',
            ]"
            v-else
            aria-hidden="true"
          />
        </button>
      </div>

      <div
        v-if="option === 1 || option === 8"
        class="mt-6 grid grid-cols-1"
        :class="[
          isTile
            ? 'gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8'
            : '',
        ]"
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
              <div class="mt-4 relative float-right" v-if="mod">
                <!-- Delete given review -->
                <button @click="deleteReview(review[0].review)">
                  <XIcon class="h-5 w-5 text-red-600" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div
        v-else
        class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8"
      >
        <div
          v-for="comment in reviews"
          :key="reviews.indexOf(comment)"
          class="group relative py-2 px-3 shadow-md dark:ring-gray-400 dark:ring-1 dark:rounded"
        >
          <div class="mt-2">
            <div class="relative">
              <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                <span>{{ comment.comment }}</span>
              </p>
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
import {
  XIcon,
  ViewListIcon,
  ViewGridIcon,
} from "@heroicons/vue/outline";
import axios from "axios";

let query = "";

const optionsToField = {
  2: "Teaching Style",
  3: "Grading Style",
  4: "Teacher Feedback",
  5: "Workload",
  6: "Assignment Style",
  7: "Exam Style",
  8: "Show all reviews",
};
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
        {
          id: 8,
          name: "Show all reviews",
        },
      ],
    };
  },
  props: {
    course: String, // passed as stringified Object, needs to be parsed
  },
  components: {
    Search,
    Pagination,
    SelectReviewMenu,
    XIcon,
    ViewListIcon,
    ViewGridIcon,
  },
  mounted() {
    // Retrieves reviews for the given course from the DB through the API, to display
    let api_link = `https://jhcourserevu-api-test.herokuapp.com/course/review/api/${
      JSON.parse(this.course).id
    }`;
    // let api_link = `http://127.0.0.1:8000/course/review/api/${JSON.parse(this.course).id}/`;

    const field = optionsToField[this.option];

    if (field != undefined) api_link += field;
    axios.get(api_link).then((response) => {
      const data = response.data;
      this.reviews = data.results;
      this.reviewCount = data.count;
      this.totalPages = Math.ceil(this.reviewCount / 10);
    });
    console.log(this.course);
  },
  methods: {
    updateOption(e: any) {
      if (e === undefined) return;

      this.option = e.id;
      const field = optionsToField[this.option];

      // let api_link = `http://127.0.0.1:8000/course/review/${JSON.parse(this.course).id}/`;
      let api_link = `https://jhcourserevu-api-test.herokuapp.com/course/review/${
        JSON.parse(this.course).id
      }/`;

      if (field != undefined && field != "Show all reviews") {
        // api_link = `http://127.0.0.1:8000/course/review/${JSON.parse(this.course).id}/${field}`;
        api_link = `https://jhcourserevu-api-test.herokuapp.com/course/review/${
          JSON.parse(this.course).id
        }/${field}`;
      }

      if (field === "Show all reviews")
        // api_link = `http://127.0.0.1:8000/course/review/api/${JSON.parse(this.course).id}/`;
        api_link = `https://jhcourserevu-api-test.herokuapp.com/course/review/api/${
          JSON.parse(this.course).id
        }/`;

      axios.get(api_link).then((response) => {
        const data = response.data;
        this.reviews = data.results;
        this.reviewCount = data.count;
        this.totalPages = Math.ceil(this.reviewCount / 10);
      });
    },
    changePage(e: number) {
      this.page = e;
      axios
        .get(
          `https://jhcourserevu-api-test.herokuapp.com/course/review/api/${
            // `http://127.0.0.1:8000/course/review/api/${
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
          // `http://127.0.0.1:8000/course/review/api/${id}/`
        )
        .then(() => {
          // Reload page with updated review list (same page unless deletion reduces # of pages)
          if (this.page === this.totalPages && this.reviewCount % 10 === 1) {
            this.page -= 1;
          }
          axios
            .get(
              `https://jhcourserevu-api-test.herokuapp.com/course/review/api/${
                // `http://127.0.0.1:8000/course/review/api/${
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
  },
});
</script>
