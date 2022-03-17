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
      <li>
        <button
          :disabled="isSelected(1)"
          class="py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 disabled:bg-gray-100 disabled:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:disabled:bg-gray-700 dark:disabled:text-white cursor-pointer"
          @click="goToPage(1)"
        >
          1
        </button>
      </li>
      <li>
        <button
          :disabled="isSelected(2)"
          class="py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 disabled:bg-gray-100 disabled:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:disabled:bg-gray-700 dark:disabled:text-white cursor-pointer"
          @click="goToPage(2)"
        >
          2
        </button>
      </li>
      <li>
        <button
          :disabled="isSelected(3)"
          class="py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 disabled:bg-gray-100 disabled:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:disabled:bg-gray-700 dark:disabled:text-white cursor-pointer"
          @click="goToPage(3)"
        >
          3
        </button>
      </li>
      <li>
        <button
          :disabled="isSelected(4)"
          class="py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 disabled:bg-gray-100 disabled:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:disabled:bg-gray-700 dark:disabled:text-white cursor-pointer"
          @click="goToPage(4)"
        >
          4
        </button>
      </li>
      <li>
        <button
          :disabled="isSelected(5)"
          class="py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 disabled:bg-gray-100 disabled:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:disabled:bg-gray-700 dark:disabled:text-white cursor-pointer"
          @click="goToPage(5)"
        >
          5
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

// let page = 1;
const maxPage = 5;

export default defineComponent({
  name: "Pagination",
  data() {
    return {
      page: 1,
    };
  },
  components: { ChevronLeftIcon, ChevronRightIcon },
  methods: {
    nextPage() {
      if (this.page < maxPage) {
        this.page += 1;
        this.$emit('change-page', this.page);
      }
    },
    prevPage() {
      if (this.page > 1) {
        this.page -= 1;
        this.$emit('change-page', this.page);
      }
    },
    goToPage(e: number) {
      this.page = e;
      this.$emit('change-page', this.page);
    },
    isSelected(index: number) {
      if (this.page === index) {
        return true;
      }
      return false;
    },
  },
});
</script>
