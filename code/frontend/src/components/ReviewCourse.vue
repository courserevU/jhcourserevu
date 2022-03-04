<template>
    <!-- page title -->
    <div class="flex space-x-2 justify-center">
        <div>
            <h1 class="text-5xl font-medium leading-tight text-gray-800 mb-3 mt-0">Course Review</h1>
        </div>
    </div>

    <!-- Class Title -->
    <div class="flex space-x-2 justify-left px-20">
        <h3 class="text-3xl font-medium leading-tight text-gray-800 mb-3 mt-0">Class: {{ course }}</h3>
    </div>

    <!-- Semseter and Professor Fields -->
    <div class="flex space-x-10 justify-">
        <!-- Professor -->
        <div class="form-group mb-3 w-1/2 px-20">
            <input
                type="text"
                class="form-control block w-full px-5 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                id="exampleInput7"
                placeholder="Professor"
            />
        </div>
        <!-- Semseter -->
        <Dropdown />
    </div>

    <!-- Review Text -->
    <div class="flex space-x-2 justify-left px-20">
        <div class="form-group mb-3 w-full ">
            <textarea
                required
                class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                id="exampleFormControlTextarea13"
                rows="3"
                placeholder="Review"
            ></textarea>
        </div>
    </div>

    <!-- Submit Button -->
    <div class="flex space-x-2 justify-center w-full">
        <div class="p-4 ...">
            <button
                type="submit"
                class="w-full px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
            >Send</button>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Dropdown from './Dropdown.vue';

export default defineComponent({
    components: { Dropdown },
    props: {
        course: String,
    }
})
</script>



