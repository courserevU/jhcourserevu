<template>
  <div class="bg-white">
    <div class="max-w-2xl mx-auto py-16 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8">
      <div>
        <Search />
      </div>

      <h2 class="text-2xl font-extrabold tracking-tight text-gray-900">Courses</h2>

      <div class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
        <div v-for="course in courses" :key="course.id" class="group relative">
          <div
            class="w-full min-h-80 bg-gray-200 aspect-w-1 aspect-h-1 rounded-md overflow-hidden group-hover:opacity-75 lg:h-80 lg:aspect-none"
          >
            <img
              :src="course.imageSrc"
              :alt="course.imageAlt"
              class="w-full h-full object-center object-cover lg:w-full lg:h-full"
            />
          </div>
          <div class="mt-4 flex justify-between">
            <div>
              <h3 class="text-sm text-gray-700">
                <a :href="course.href">
                  <span aria-hidden="true" class="absolute inset-0" />
                  {{ course.name }}
                </a>
              </h3>
              <p class="mt-1 text-sm text-gray-500">{{ course.color }}</p>
            </div>
            <p class="text-sm font-medium text-gray-900">{{ course.price }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Search from './Search.vue';

const courses = [
  {
    id: 1,
    name: 'Object-Oriented Software Engineering',
    href: '#',
    imageSrc: 'https://www.kappit.com/img/pics/47808748bfbcc_sm.png',
    imageAlt: "The face I make when I think of OOSE.",
    price: '601.421',
    color: 'Computer Science',
  },
  // More courses... load from our db
]

export default defineComponent({
  name: "CourseDisplay",
  setup() {
    return {
      courses,
    };
  },
  components: { Search }
});
</script>