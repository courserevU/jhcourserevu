<template>
  <div class="flex flex-col h-screen">
    <NavBar />
    <LoginBox class="flex-grow" v-bind:login="false" />
    <Footer />
  </div>
</template>

<script setup lang="ts">
import NavBar from "../components/NavBar.vue";
import Footer from "../components/Footer.vue";
import LoginBox from "../components/LoginBox.vue";
</script>