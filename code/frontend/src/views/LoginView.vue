<template>
  <NavBar />
  <LoginBox  v-bind:login="true">
  </LoginBox>
  <Footer />
</template>

<script setup lang="ts">
import NavBar from "../components/NavBar.vue";
import Footer from "../components/Footer.vue";
import LoginBox from "../components/LoginBox.vue"
</script>