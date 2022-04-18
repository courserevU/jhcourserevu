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
      </div>

      <div
        class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8"
      >
        <div
          v-for="course in filteredCourses"
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
    axios.get(`https://jhcourserevu-api-test.herokuapp.com/course/api/`)
      .then((response) => {
        const data = response.data;
        this.courses = data.results;
      })

    // axios.get(`http://localhost:8000/course/api/`)
    //   .then((response) => {
    //     const data = response.data;
    //     this.courses = data.results;
    //     console.log(JSON.parse(JSON.stringify(data.results)));
    //   })
  },
  methods: {
    updateFilter(e: any) {
      this.query = e;
    },
    updateOption(e: any) {
      this.option = e.id;
    },
    changePage(e: number) {
      this.page = e;

      // Gets correct page of courses via API page query
      axios.get(`https://jhcourserevu-api-test.herokuapp.com/course/api/?page=${this.page}`)
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
    filteredCourses() {
      const field = optionsToField[this.option];
    
      if (field === undefined) return this.courses;
      
      return this.courses.filter(
        course => {
          return course[field].toLowerCase().includes(this.query.toLowerCase());
        });
    },
  },
});
</script>