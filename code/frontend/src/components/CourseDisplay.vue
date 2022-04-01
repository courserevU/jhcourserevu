<template>
  <div class="bg-white dark:bg-gray-800">
    <div class="max-w-2xl mx-auto py-16 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8">
      <div class ="flex flex-row space-x-3">
        <Search @update-filter="updateFilter" />
        <SelectMenu :options=filters />
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

      <h2 class="text-2xl font-extrabold tracking-tight text-gray-900 dark:text-gray-200">Courses</h2>

      <div class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
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
              <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">{{ course.department }} - {{ course.number }}</p>
            </div>
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
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Search from './Search.vue';
import SelectMenu from "./SelectMenu.vue";

let courses = [
  {
    id: 1,
    name: 'Object-Oriented Software Engineering',
    href: '#',
    number: '601.421',
    department: 'Computer Science',
  },
  {
    id: 2,
    name: 'Data Structures',
    href: '#',
    number: '601.226',
    department: 'Computer Science',
  },
  {
    id: 3,
    name: 'Introduction to Cognitive Psychology',
    href: '#',
    number: '200.110',
    department: 'Psychological & Brain Sciences'
  },
  {
    id: 4,
    name: 'Guided Tour: The Planets',
    href: '#',
    number: '270.114',
    department: 'Earth & Planetary Sciences'
  },
  {
    id: 5,
    name: 'Probability & Statistics for the Physical Sciences & Engineering',
    href: '#',
    number: '553.310',
    department: 'Applied Mathematics and Statistics'
  },
  {
    id: 6,
    name: 'Planetary Surface Processes',
    href: '#',
    number: '270.410',
    department: 'Earth & Planetary Sciences'
  }
  // More courses... load from our db
];

let query = "";

export default defineComponent({
  name: "CourseDisplay",
  data() {
    return {
      query,
      courses,
      filters: [
        {
            id: 1,
            name: 'Please Choose an Option',
        },
        {
            id: 2,
            name: 'Placeholder1',
        },
        {
            id: 3,
            name: 'Placeholder2',
        },
        {
            id: 4,
            name: 'Placeholder3',
        }
      ]
    }
  },
  components: { Search, SelectMenu },
  methods: {
    updateFilter(e: any) {
      this.query = e;
    },
    goToWriteReview(course: any) {
      this.$router.push({ name: "write", params: { course: course.name } });
    },
    goToReadReviews(course: any) {
      this.$router.push({ name: "read", params: { course: course.name } });
    }
  },
  computed: {
    filteredCourses() {
      return this.courses.filter((course: any) => {
        return this.query.toLowerCase().split(" ")
          .every(v => course.name.toLowerCase().includes(v) || course.number.toLowerCase().includes(v));
      });
    },
  },
});
</script>