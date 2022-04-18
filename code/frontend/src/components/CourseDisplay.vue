<template>
  <div class="bg-white dark:bg-gray-800">
    <div class="max-w-2xl mx-auto py-16 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8">

      <h2
        class="text-2xl font-extrabold tracking-tight text-gray-900 dark:text-gray-200 mb-4"
      >
        Courses
      </h2>

      <!-- Search Bar + Dropdown for more specific search -->
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
          v-for="course in this.courses"
          :key="course.id"
          class="group relative py-2 px-3 shadow-md dark:ring-gray-400 dark:ring-1 dark:rounded"
        >
          <div class="mt-2 flex">
            <div class="justify-left">
              <h3 class="text-sm text-gray-700 dark:text-gray-300">
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
            <Checkbox label="I have taken this course" inputValue="taken" v-model="selectedOptions" />
          </div>
          <div class="block inline-flex mt-4 mb-2">
            <button
              type="button"
              class="bg-blue-500 hover:bg-blue-700 dark:bg-blue-700 dark:hover:bg-blue-900 text-white dark:text-gray-200 font-bold py-1 px-2 mx-1 rounded"
              @click="goToWriteReview(course)"
            >Write Review</button>
            <button
              type="button"
              class="bg-blue-500 hover:bg-blue-700 dark:bg-blue-700 dark:hover:bg-blue-900 text-white dark:text-gray-200 font-bold py-1 px-2 mx-1 rounded"
              @click="goToReadReviews(course)"
            >Read Reviews</button>
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
import { defineComponent } from 'vue';
import Search from './Search.vue';
import SelectMenu from "./SelectMenu.vue";
import Pagination from "./Pagination.vue";
import Checkbox from "./Checkbox.vue";
import axios from "axios";


let courses = [];

let query = "";
let option = "";

const optionsToField = {
  2 : "name",
  3 : "course_num",
  4 : "department"
};

export default defineComponent({
  name: "CourseDisplay",
  data() {
    return {
      query,
      option,
      courses,
      filters: [
        {
            id: 2,
            name: 'Course Name',
        },
        {
            id: 3,
            name: 'Course Number',
        },
        {
            id: 4,
            name: 'Department',
        }
      ],
      page: 1,
    }
  },
  components: { Search, SelectMenu, Pagination, Checkbox },
  mounted() {
    // axios.get(`https://jhcourserevu-api-test.herokuapp.com/course/api/`)
    //   .then((response) => {
    //     const data = response.data;
    //     this.courses = data.results;
    //   })

    axios.get(`http://localhost:8000/course/api/`)
      .then((response) => {
        const data = response.data;
        this.courses = data.results;
        // console.log(JSON.parse(JSON.stringify(data.results)));
      })
  },
  methods: {
    updateFilter(e: any) {
      if(e === undefined) return;

      this.query = e;
      console.log("this.option", this.option);
      console.log("query = ", this.query);

      const field = optionsToField[this.option];
      console.log("field", field);
      
      // let api_link = `https://jhcourserevu-api-test.herokuapp.com/course/api/`;
      let api_link = `http://127.0.0.1:8000/course/api/`;

      if (field != undefined && this.query != "")
        api_link = `http://127.0.0.1:8000/course/search/${field}/?q=${this.query}`;

      // Gets correct page of courses via API page query
      axios.get(api_link)
      .then((response) => {
        const data = response.data;
        this.courses = data.results;
      })
    },
    updateOption(e: any) {
      if(e === undefined) return;

      this.option = e.id;
      console.log("updateOption")
      console.log("query = ", this.query);

      this.updateFilter(this.query);
    },
    changePage(e: number) {
      this.page = e;

      // Gets correct page of courses via API page query

      // let api_link = `https://jhcourserevu-api-test.herokuapp.com/course/api/?page=${this.page}`;
      let api_link = `http://127.0.0.1:8000/course/api/?page=${this.page}`;

      const field = optionsToField[this.option];

      if (field != undefined && this.query != "")
        api_link = `http://127.0.0.1:8000/course/search/${field}/?q=${this.query}&&page=${this.page}`;
      
      axios.get(api_link)
      .then((response) => {
        const data = response.data;
        this.courses = data.results;
      })
    },
    goToWriteReview(course: any) {
      this.$router.push({ name: "write", params: { "course": JSON.stringify(course) } });
    },
    goToReadReviews(course: any) {
      this.$router.push({ name: "read", params: { "course": JSON.stringify(course) } });
    },
  },
  
  computed: {
    // filteredCourses() {
    //   const field = optionsToField[this.option];
    
    //   if (field === undefined) return this.courses;
      
      

      // return this.courses.filter(
      //   course => {
      //     return course[field].toLowerCase().includes(this.query.toLowerCase());
      //   });
    // },
  },
});
</script>