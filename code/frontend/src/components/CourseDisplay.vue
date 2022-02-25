<template>
  <div class="bg-white">
    <div class="max-w-2xl mx-auto py-16 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8">
      <div>
        <Search @update-filter="updateFilter" />
      </div>

      <h2 class="text-2xl font-extrabold tracking-tight text-gray-900">Courses</h2>

      <div class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
        <div v-for="course in filteredCourses" :key="course.id" class="group relative">
          <div class="mt-4 flex justify-between">
            <div>
              <h3 class="text-sm text-gray-700">
                <a :href="course.href">
                  <span aria-hidden="true" class="absolute inset-0" />
                  {{ course.name }}
                </a>
              </h3>
              <p class="mt-1 text-sm text-gray-500">{{ course.department }}</p>
            </div>
            <p class="text-sm font-medium text-gray-900">{{ course.number }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Search from './Search.vue';

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
  components: { Search },
  methods: {
    updateFilter(e: any) {
      this.query = e;
    },
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