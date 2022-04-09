<template>
  <div class="flex justify-left">
    <div class="mb-3 xl:w-96">
      <div class="input-group relative flex items-stretch w-full mb-4 rounded">
        <input
          type="search"
          class="form-control relative flex-auto min-w-0 block w-full px-3 py-1.5 text-base font-normal text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-800 bg-clip-padding border border-solid border-gray-300 dark:border-gray-300 rounded transition ease-in-out m-0 focus:border-blue-400 focus:outline-none"
          placeholder="Search"
          aria-label="Search"
          aria-describedby="button-addon2"
          v-model="query"
          @input="$emit('update-filter', query)"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: "Search",
  data() {
    return {
      query: ""
    }
  },
});
</script>