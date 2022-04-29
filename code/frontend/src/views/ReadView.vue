<template>
  <div class="flex flex-col h-screen">
    <NavBar />
    <ReviewDisplay class="flex-grow" v-bind:course="course" />
    <Footer />
  </div>
</template>

<script lang="ts">
import NavBar from "../components/NavBar.vue";
import Footer from "../components/Footer.vue";
import ReviewDisplay from "../components/ReviewDisplay.vue";
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      course: String,
    };
  },
  created() {
    this.course = this.$route.params.course;
  },
  components: { NavBar, Footer, ReviewDisplay },
});
</script>
