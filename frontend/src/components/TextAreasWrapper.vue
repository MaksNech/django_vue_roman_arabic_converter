<template>
    <div>
      <p class="error" v-if="err">Invalid input format error. Verify that the input is correct.</p>
        <div class="row">
            <div class="col">
                <numeric-text-area @convertInt="convertInt" :value="firstInput" :id="1" ></numeric-text-area>
            </div>
            <div class="col">
                <numeric-text-area @convertInt="convertInt" :value="secondInput" :id="2" :readOnly="true" ></numeric-text-area>
            </div>
        </div>
    </div>
</template>


<script>
import NumericTextArea from "./NumericTextArea";
import debounce from "lodash";

export default {
  name: "textAreaWrapper",
  components: {
    NumericTextArea: NumericTextArea
  },
  data() {
    return {
      firstInput: "",
      secondInput: "",
      err: false
    };
  },
  methods: {
    convertInt: _.debounce(function(e) {
      if (e.num_value == "") {
        if (e.id == 1) {
          this.secondInput = e.num_value;
        } else {
          this.firstInput = e.num_value;
        }
      } else {
        this.sendData(e);
      }
    }, 500),
    sendData: function(data) {
      $.ajax({
        url: "http://localhost:8000/api/converter/",
        headers: { "X-CSRFToken": $.cookie("csrftoken") },
        type: "POST",
        dataType: "json",
        data: data,
        success: response => {
          this.err = false;
          if (data.id == 1) {
            this.secondInput = response.num_value;
          } else {
            this.firstInput = response.num_value;
          }
        },
        error: (xhr, errMsg, err) => {
          this.err = true;
          console.error(err);
        }
      });
    }
  }
};
</script>
<style>
</style>