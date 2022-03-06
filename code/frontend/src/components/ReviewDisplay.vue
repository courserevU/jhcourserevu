<template>
  <div class="bg-white dark:bg-gray-800">
    <div class="max-w-2xl mx-auto py-16 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8">

      <h2 class="text-2xl font-extrabold tracking-tight text-gray-900 dark:text-gray-200">Reviews for {{ course }}</h2>

      <div class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
        <div
          v-for="review in reviews"
          :key="review.id"
          class="group relative py-2 px-3 shadow-md dark:shadow-gray-600"
        >
          <div class="mt-2 flex justify-left">
            <div>
              <h3 class="text-md text-gray-700 dark:text-gray-300">
                <a>
                  Professor: {{ review.professor }}
                </a>
              </h3>
              <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">{{ review.review }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Search from './Search.vue';

let reviews = [
  {
    id: 1,
    professor: "Ali Madooei",
    review: "Greatest teaching ever!",
  },
  {
    id: 2,
    professor: "Imaginary Professor",
    review: "Entirely self-directed class - the professor never appeared!",
  },
  {
    id: 3,
    professor: "Mr. Anderson",
    review: "We live in a simulation.",
  }
  // More reviews... load from our db
];

let query = "";

export default defineComponent({
  name: "ReviewDisplay",
  data() {
    return {
      query,
      reviews,
    }
  },
  props: {
    course: String,
  },
  methods: {
    goToWriteReview(course: any) {
      this.$router.push({ path: "/write", name: "write", params: { course: course } });
    },
    goToReadReviews(course: any) {
      this.$router.push({ name: "read", params: { course: course } });
    }
  }
});
</script>