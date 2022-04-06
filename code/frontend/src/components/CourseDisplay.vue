<template>
  <div class="bg-white dark:bg-gray-800">
    <div
      class="max-w-2xl mx-auto py-16 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8"
    >
      <div>
        <Search @update-filter="updateFilter" />
      </div>

      <h2
        class="text-2xl font-extrabold tracking-tight text-gray-900 dark:text-gray-200"
      >
        Courses
      </h2>

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
                  {{ course.name }}
                </a>
              </h3>
              <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">
                {{ course.department }} - {{ course.number }}
              </p>
            </div>
          </div>
          <Checkbox label="React" inputValue="react" v-model="selectedOptions" />
          <div class="block inline-flex mt-4 mb-2">
            <button
              type="button"
              class="bg-blue-500 hover:bg-blue-700 dark:bg-blue-700 dark:hover:bg-blue-900 text-white dark:text-gray-200 font-bold py-1 px-2 mx-1 rounded"
              @click="goToWriteReview(course)"
            >
              Write Review
            </button>
            <button
              type="button"
              class="bg-blue-500 hover:bg-blue-700 dark:bg-blue-700 dark:hover:bg-blue-900 text-white dark:text-gray-200 font-bold py-1 px-2 mx-1 rounded"
              @click="goToReadReviews(course)"
            >
              Read Reviews
            </button>
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
import Checkbox from "./Checkbox.vue";

let courses = [
  {
    id: 1,
    name: "Object-Oriented Software Engineering",
    href: "#",
    number: "601.421",
    department: "Computer Science",
    page: 1,
  },
  {
    id: 2,
    name: "Data Structures",
    href: "#",
    number: "601.226",
    department: "Computer Science",
    page: 1,
  },
  {
    id: 3,
    name: "Introduction to Cognitive Psychology",
    href: "#",
    number: "200.110",
    department: "Psychological & Brain Sciences",
    page: 1,
  },
  {
    id: 4,
    name: "Guided Tour: The Planets",
    href: "#",
    number: "270.114",
    department: "Earth & Planetary Sciences",
    page: 1,
  },
  {
    id: 5,
    name: "Probability & Statistics for the Physical Sciences & Engineering",
    href: "#",
    number: "553.310",
    department: "Applied Mathematics and Statistics",
    page: 2,
  },
  {
    id: 6,
    name: "Planetary Surface Processes",
    href: "#",
    number: "270.410",
    department: "Earth & Planetary Sciences",
    page: 2,
  },
  // More courses... load from our db
];

let query = "";

export default defineComponent({
  name: "CourseDisplay",
  data() {
    return {
      query,
      courses,
      page: 1,
    };
  },
  components: { Search, Pagination, Checkbox },
  methods: {
    updateFilter(e: any) {
      this.query = e;
    },
    changePage(e: number) {
      this.page = e;
    },
    goToWriteReview(course: any) {
      this.$router.push({ name: "write", params: { course: course.name } });
    },
    goToReadReviews(course: any) {
      this.$router.push({ name: "read", params: { course: course.name } });
    },
  },
  computed: {
    filteredCourses() {
      return this.courses.filter((course: any) => {
        return (course.page === this.page) && this.query
          .toLowerCase()
          .split(" ")
          .every(
            (v) =>
              course.name.toLowerCase().includes(v) ||
              course.number.toLowerCase().includes(v)
          );
      });
    },
  },
});
</script>