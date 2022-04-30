<template>
  <label>
    <input type="checkbox" v-model="model" />
    <span>{{ " " + label }}</span>
    <!-- <input type="checkbox" id="checkbox" v-model="checked">
            <label for="checkbox">{{ checked }}</label> -->
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
