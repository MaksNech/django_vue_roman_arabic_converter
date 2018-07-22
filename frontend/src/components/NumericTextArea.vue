<template>
      <form action="#">
        <label id="labelTextArea" v-bind:class="{ error: inputError }">{{label}}</label>
        <textarea v-model="num_val" v-on:keyup="onValueChange" class="form-control" ref="TextArea" rows="10"></textarea>
      </form>
</template>

<script>
export default {
  name: "NumericTextArea",
  props: ["value", "id"],
  data() {
    return {
      num_val: "",
      label: "Type here numeral",
      inputError: false
    };
  },
  watch: {
    value: {
      immediate: true,
      handler(newVal, oldVal) {
        this.num_val = newVal.toString();
        this.checkInputType(this.num_val);
      }
    }
  },
  methods: {
    onValueChange: function(event) {
      if (this.checkInputType(this.num_val)) {
        this.$emit("convertInt", {
          num_value: this.num_val,
          label: this.label,
          id: this.id
        });
      }
    },
    checkInputType: function(value) {
      this.inputError = false;
      if (value == "") {
        this.label = "Type here numeral";
        return false;
      } else if (
        Boolean(value.match(/[^IVXLCDM]/gi)) &&
        Boolean(value.match(/[^0-9]/gi))
      ) {
        this.label = "Invalid input format error";
        this.inputError = true;
        return false;
      } else if (!Boolean(value.match(/[^0-9]/gi))) {
        this.label = "Arabic";
        return true;
      } else if (!Boolean(value.match(/[^IVXLCDM]/gi))) {
        this.label = "Roman";
        return true;
      }
    }
  }
};
</script>

<style>
textarea {
  resize: none;
}
label {
  color: #3596ff;
}
.error {
  color: red;
}
</style>
