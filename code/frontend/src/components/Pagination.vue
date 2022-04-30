<template>
  <nav aria-label="Page navigation example">
    <ul class="inline-flex items-center -space-x-px mt-8">
      <li>
        <button
          type="button"
          @click="prevPage"
          class="block py-2 px-3 ml-0 leading-tight text-gray-500 bg-white rounded-l-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white cursor-pointer"
        >
          <span class="sr-only">Previous</span>
          <ChevronLeftIcon class="h-5 w-5" aria-hidden="true" />
        </button>
      </li>
      <li v-for="index in pagesAtATime" :key="index">
        <button
          :disabled="isSelected(index + firstPage)"
          class="py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 disabled:bg-gray-100 disabled:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:disabled:bg-gray-700 dark:disabled:text-white cursor-pointer"
          @click="goToPage(index + firstPage)"
        >
          {{ index + firstPage }}
        </button>
      </li>
      <li>
        <button
          @click="nextPage"
          class="block py-2 px-3 leading-tight text-gray-500 bg-white rounded-r-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white cursor-pointer"
        >
          <span class="sr-only">Next</span>
          <ChevronRightIcon class="h-5 w-5" aria-hidden="true" />
        </button>
      </li>
    </ul>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/vue/solid";

export default defineComponent({
  name: "Pagination",
  data() {
    return {
      currentPage: 1,
      firstPage: 0,
    };
  },
  props: {
    maxPage: Number,
    pageReplacement: Number,
  },
  computed: {
    pagesAtATime() {
      return this.maxPage < 5 ? this.maxPage : 5;
    },
  },
  components: { ChevronLeftIcon, ChevronRightIcon },
  methods: {
    nextPage() {
      if (this.currentPage < this.maxPage) {
        this.currentPage += 1;
        if (this.firstPage < this.maxPage - 5 && this.currentPage > 3) {
          this.firstPage += 1;
        }
        this.$emit("change-page", this.currentPage);
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1;
        if (this.firstPage > 0 && this.currentPage > 2) {
          this.firstPage -= 1;
        }
        this.$emit("change-page", this.currentPage);
      }
    },
    goToPage(e: number) {
      this.currentPage = e;

      if (this.currentPage > 2 && this.currentPage < this.maxPage - 2) {
        this.firstPage = this.currentPage - 3;
      } else if (this.currentPage > 1 && this.currentPage < this.maxPage - 2) {
        this.firstPage = this.currentPage - 2;
      }

      this.$emit("change-page", this.currentPage);
    },
    isSelected(index: number) {
      if (this.pageReplacement) {
        this.currentPage = this.pageReplacement; // in case of review deletion
      }
      if (this.currentPage === index) {
        return true;
      }
      return false;
    },
  },
});
</script>
