<template>
  <NavBar />
  <ReviewCourse v-bind:course="course" />
  <Footer />
</template>

<script lang="ts">
import NavBar from "../components/NavBar.vue";
import Footer from "../components/Footer.vue";
import ReviewCourse from "../components/ReviewCourse.vue";
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      course: String,
    }
  },
  created() {
    this.course = this.$route.params.course
  },
  components: { NavBar, Footer, ReviewCourse },
});
</script>