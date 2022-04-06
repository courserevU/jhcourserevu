<template>
    <label>
        <input  type="checkbox" :value="inputValue"  v-model="model" />
        <span>{{ " " + label }}</span>
    </label>
</template>

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