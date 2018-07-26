<template>
      <form action="#">
        <label class="rt" id="labelTextArea" v-bind:class="{ error: inputError }">{{label}}</label>
        <textarea 
        class="form-control" 
        ref="TextArea" 
        rows="10"
        :readonly="readOnly"
        v-model="num_val" 
        v-on:keyup="onValueChange" 
        ></textarea>
      </form>
</template>

<script>
export default {
  name: "NumericTextArea",
  props: ["value", "id", "readOnly"],
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
        return true;
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
