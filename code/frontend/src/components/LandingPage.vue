<template>
  <div>
    <main
      class="h-screen flex items-center px-6 lg:px-32 bg-gradient-to-b from-blue-600 to-blue-200 dark:to-grey-900 text-white relative"
    >
      <section class="w-full md:w-9/12 xl:w-8/12">
        <h1 class="text-3xl lg:text-5xl font-extrabold text-white-500">
          JHcourserevU
        </h1>
        <br />
        <p class="font-bold mb-1">
          Review courses at JHU (Johns Hopkins University)
        </p>
        <br />
        <p>
          Evaluate courses and share your feedback to guide fellow students'
          semesterly schedules.
        </p>
        <br />
        <button
          type="submit"
          class="w-1/2 px-10 py-2.5 justify-center bg-gray-200 dark:bg-gray-700 text-black dark:text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-200 dark:hover:bg-blue-100 hover:shadow-lg focus:bg-blue-300 dark:focus:bg-blue-400 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
          @click="goToCourseSeach"
        >
          Seach for Courses!
        </button>
      </section>

      <!-- <footer class="absolute right-0 bottom-0 p-6 lg:p-32">
                <p class="font-bold mb-1">Yours Truly</p>
                <p>Contact Info</p>
            </footer> -->
    </main>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  methods: {
    goToCourseSeach() {
      this.$router.push("/course-search");
    },
  },
});
</script>
