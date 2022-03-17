<template>
    <div>
        <main class="h-screen flex items-center px-6 lg:px-32 bg-blue-900 text-white relative">
            <section class="w-full md:w-9/12 xl:w-8/12">
               
                <h1 class="text-3xl lg:text-5xl font-bold text-white-500">
                    JHcourserevU
                </h1>
                <br/>
                <p class="font-bold mb-1">
                    JHcourserevU is an application to rate, review, and view reviews for the courses right here at JHU.
                </p>
                <br/>
                <p>
                    This website would provide a simple and intuitive platform for students to rate and write reviews for the courses at Johns Hopkins University. 
                    They could also directly view all reviews and ratings and have a guarantee they are reading a completely valid review/rating. 
                    It would be appropriately moderated, open source, and affiliated with Semesterly so as to guarantee that it could be sustainable..
                </p>
                <br/>
                <button
                    type="submit"
                    class="w-1/2 px-10 py-2.5 justify-center bg-gray-400 dark:bg-gray-700 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-200 dark:hover:bg-blue-100 hover:shadow-lg focus:bg-blue-300 dark:focus:bg-blue-400 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                    @click="goToCourseSeach"
                >Seach for Courses!</button>
            </section>
            
            <footer class="absolute right-0 bottom-0 p-6 lg:p-32">
                <p class="font-bold mb-1">Yours Truly</p>
                <p>Contact Info</p>
            </footer>
        </main>
        
    </div>

</template>
<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
  methods: {
    goToCourseSeach() {
      this.$router.push("/course-search");
    }
  }
});
</script>