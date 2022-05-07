<template>
  <div class="bg-white dark:bg-gray-800">
    <div
      class="max-w-2xl mx-auto py-16 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8"
    >
      <h2
        class="text-2xl font-extrabold tracking-tight text-gray-900 dark:text-gray-200 mb-4"
      >
        Courses
      </h2>

      <!-- Search Bar + Dropdown for more specific search -->
      <div class="flex flex-row space-x-3">
        <Search @update-filter="updateFilter" />
        <SelectMenu :options="filters" @update-option="updateOption" />
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
        class="mt-6 grid grid-cols-1"
        :class="[
          isTile
            ? 'gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8'
            : '',
        ]"
      >
        <div
          v-for="course in this.courses"
          :key="course.id"
          class="group relative py-2 px-3 shadow-md dark:ring-gray-400 dark:ring-1 dark:rounded"
        >
          <div class="mt-2 px-2 flex">
            <div class="justify-left">
              <h3 class="text-md font-bold text-gray-700 dark:text-gray-300">
                <a>
                  <span aria-hidden="true" class="inset-0" />
                  {{ course.name }} ({{ course.meeting_section }})
                </a>
              </h3>
              <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                {{ course.department }} - {{ course.course_num }}
              </p>
              <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                {{ course.semester }}
              </p>
            </div>
          </div>
          <div class="mt-2">
            <input
              v-show = "this.user_id"
              type="checkbox"
              :id="course.course_num"
              :value="course"
              v-model="taken"
              @change="updateTakenStatus(course)"
            />
            <label
              v-show = "this.user_id"
              for="checkbox"
              class="text-sm text-gray-700 dark:text-gray-300"
              >{{ " I have taken this course" }}</label
            >
          </div>
          <div class="block inline-flex mt-4 mb-2">
            <button
              type="button"
              class="bg-blue-500 hover:bg-blue-700 dark:bg-blue-700 dark:hover:bg-blue-900 text-white dark:text-gray-200 font-bold py-1 px-3 mx-1 rounded"
              @click="goToReadReviews(course)"
            >
              <EyeIcon class="float-left h-5 w-5 mr-2 mt-0.5" />
              Read Reviews
            </button>
            <button
              v-if="haveTakenCourse(course)"
              type="button"
              class="bg-blue-500 hover:bg-blue-700 dark:bg-blue-700 dark:hover:bg-blue-900 text-white dark:text-gray-200 font-bold py-1 px-3 mx-1 rounded"
              @click="goToWriteReview(course)"
            >
              <PlusIcon class="float-left h-5 w-5 mr-2 mt-0.5" />
              Write Review
            </button>
          </div>
        </div>
      </div>
      <div>
        <Pagination @change-page="changePage" :maxPage="totalPages" :pageReplacement="page" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { EyeIcon, PlusIcon } from "@heroicons/vue/solid";
import Search from "./Search.vue";
import SelectMenu from "./SelectMenu.vue";
import Pagination from "./Pagination.vue";
import Checkbox from "./Checkbox.vue";
import axios from "axios";
import { ViewGridIcon, ViewListIcon } from "@heroicons/vue/outline";
let taken = [];
let courses = [];

let query = "";
let option = "";

const optionsToField = {
  2: "name",
  3: "course_num",
  4: "department",
};

export default defineComponent({
  name: "CourseDisplay",
  data() {
    return {
      user_id: "",
      query,
      option,
      taken,
      courses,
      filters: [
        {
          id: 2,
          name: "Course Name",
        },
        {
          id: 3,
          name: "Course Number",
        },
        {
          id: 4,
          name: "Department",
        },
      ],
      page: 1,
      totalPages: 5,
      isTile: true,
    };
  },
  mounted() {
    window.addEventListener("localstorage-changed", (event) => {
      this.user_id = JSON.parse(event.detail.user);
      if (this.user_id) {
        // http://localhost:8000/user/api/id/${this.user_id}
        // https://jhcourserevu-api-test.herokuapp.com/user/api/id/${this.user_id}
        axios
          .get(
            `https://jhcourserevu-api-test.herokuapp.com/user/api/id/${this.user_id}`
          )
          .then((response) => {
            const data = response.data;
            this.taken = data.results;
          });
      } else {
        this.taken = [];
      }
    });

    if (localStorage.getItem("user_id")) {
      this.user_id = JSON.parse(localStorage.getItem("user_id"));
    }

    if (this.user_id) {
      // https://jhcourserevu-api-test.herokuapp.com/user/api/id/${this.user_id}
      // http://localhost:8000/user/api/id/${this.user_id}
      axios
        .get(
          `https://jhcourserevu-api-test.herokuapp.com/user/api/id/${this.user_id}`
        )
        .then((response) => {
          const data = response.data;
          this.taken = data.results;
          axios
            .get(`https://jhcourserevu-api-test.herokuapp.com/course/api/`)
            .then((response) => {
              const data = response.data;
              this.courses = data.results;
              this.totalPages = Math.ceil(data.count / 10);
            });
        });
    } else {
      axios
        .get(`https://jhcourserevu-api-test.herokuapp.com/course/api/`)
        .then((response) => {
          const data = response.data;
          this.courses = data.results;
          this.totalPages = Math.ceil(data.count / 10);
        });
    }

    
    
  },
  components: {
    Search,
    SelectMenu,
    Pagination,
    Checkbox,
    EyeIcon,
    PlusIcon,
    ViewListIcon,
    ViewGridIcon,
  },
  methods: {
    updateFilter(e: any) {
      if (e === undefined) return;

      this.query = e;

      const field = optionsToField[this.option];

      let api_link = `https://jhcourserevu-api-test.herokuapp.com/course/api/?page=${this.page}`;

      if (field != undefined && this.query != "") {
        this.page = 1;
        api_link = `https://jhcourserevu-api-test.herokuapp.com/course/search/${field}/?q=${this.query}`;
      }

      // Gets correct page of courses via API page query
      axios.get(api_link).then((response) => {
        const data = response.data;
        this.courses = data.results;
        this.totalPages = Math.ceil(data.count / 10);
      });
    },
    updateOption(e: any) {
      if (e === undefined) return;

      this.option = e.id;
      this.updateFilter(this.query);
    },
    changePage(e: number) {
      this.page = e;

      // Gets correct page of courses via API page query
      let api_link = `https://jhcourserevu-api-test.herokuapp.com/course/api/?page=${this.page}`;

      const field = optionsToField[this.option];

      if (field != undefined && this.query != "") {
        api_link = `https://jhcourserevu-api-test.herokuapp.com/course/search/${field}/?q=${this.query}&&page=${this.page}`;
      }

      axios.get(api_link).then((response) => {
        const data = response.data;
        this.courses = data.results;
      });
    },
    toggleLayout() {
      this.isTile = !this.isTile;
    },
    goToWriteReview(course: any) {
      this.$router.push({
        name: "write",
        params: { course: JSON.stringify(course) },
      });
    },
    goToReadReviews(course: any) {
      this.$router.push({
        name: "read",
        params: { course: JSON.stringify(course) },
      });
    },
    addCourse(course_id: any) {
      // http://localhost:8000/user/api/
      // https://jhcourserevu-api-test.herokuapp.com/user/api/
      axios
        .post(`https://jhcourserevu-api-test.herokuapp.com/user/api/`, {
          user_id: this.user_id,
          course_id: course_id,
        })
        .then((response) => {
          const data = response.data;
        });
    },
    haveTakenCourse(course: any) {
      return this.taken.some(courseTaken=> {
        if(courseTaken.id == course.id){ return true};
        return false;
      });
    },
    updateTakenStatus(course: any) {
      //if becomes unchecked take out from user's courses, otherwise add the course to user's courses
      if (this.haveTakenCourse(course)) {
        console.log("adding");
        this.addCourse(course.id);
      } else {
        axios.delete(`https://jhcourserevu-api-test.herokuapp.com/user/api/`, {
          data: {
            user_id: this.user_id,
            course_id: course.id,
          },
        });
      }
    },
  },
});
</script>
