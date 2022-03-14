<template>
  <div class="flex flex-col h-screen">
    <NavBar />
    <LandingPage class="flex-grow" />
    <Footer />
  </div>
</template>

<script setup lang="ts">
import NavBar from "../components/NavBar.vue";
import Footer from "../components/Footer.vue";
import LandingPage from "@/components/LandingPage.vue";
</script>
