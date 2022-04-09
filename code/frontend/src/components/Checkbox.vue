<template>
    <label>
<<<<<<< HEAD
        <input  type="checkbox"  v-model="model" />
        <span>{{ " " + label }}</span>
        <!-- <input type="checkbox" id="checkbox" v-model="checked">
            <label for="checkbox">{{ checked }}</label> -->
=======
        <input type="checkbox" :value="inputValue" v-model="model" />
        <span class="text-sm text-gray-700 dark:text-gray-300 font-bold">{{ " " + label }}</span>
>>>>>>> e703d3251dd970a69a369f3e4c19040ca1f6b4c9
    </label>
</template>

<!-- TODO make it so the write review button only appears when the check box has been ticked,  -->
          <!-- check from user if the user has previously ticked the box check box has been ticked -->
          <!-- have a vraiable that keeps track of the check mark -->
          <!-- only ifthe varibale is ture than check it -->
<script>
export default {
  name: "Checkbox",
  props: {
    label: String,
    value: Array,
    inputValue: String,
  },
  computed: {
    model: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  },
};
</script>