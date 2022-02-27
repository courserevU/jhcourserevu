<template>
  <div class="bg-white">
    <div class="max-w-2xl mx-auto py-16 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8">
      <div>
        <Search @update-filter="updateFilter" />
      </div>

      <h2 class="text-2xl font-extrabold tracking-tight text-gray-900">Courses</h2>

      <div class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
        <div
          v-for="course in filteredCourses"
          :key="course.id"
          class="group relative py-2 px-3 shadow-md"
        >
          <div class="mt-2 flex justify-center">
            <div>
              <h3 class="text-sm text-gray-700">
                <a>
                  <span aria-hidden="true" class="inset-0" />
                  {{ course.name }}
                </a>
              </h3>
              <p class="mt-2 text-sm text-gray-500">{{ course.department }}</p>
            </div>
            <p class="text-sm font-medium text-gray-900">{{ course.number }}</p>
          </div>
          <div class="block inline-flex mt-4 mb-2">
            <button
              type="button"
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 mx-1 rounded"
              @click="goToWriteReview(course)"
            >Write Review</button>
            <button
              type="button"
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 mx-1 rounded"
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
import Dropdown from './Dropdown.vue';

let courses = [
  {
    id: 1,
    name: 'Object-Oriented Software Engineering',
    href: '#',
    number: '601.421',
    department: 'Computer Science',
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
    }
  },
  components: { Search, Dropdown },
  methods: {
    updateFilter(e: any) {
      this.query = e;
    },
    goToWriteReview(course: any) {
      this.$router.push({ path: "/write", name: "write", params: { course: course } });
    },
    goToReadReviews(course: any) {
      this.$router.push({ name: "read", params: { course: course } });
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