<template>
  <div class="bg-white dark:bg-gray-800">
    <!-- page title -->
    <div class="py-5"></div>
    <div class="flex space-x-2 justify-center">
      <div>
        <h1
          class="text-5xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0"
        >
          Course Review
        </h1>
      </div>
    </div>
    <div class="py-5"></div>
    <!-- Class Title -->
    <div class="flex space-x-2 justify-left px-20">
      <h3
        class="text-3xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0"
      >
        Class: {{ JSON.parse(course).name }}
      </h3>
    </div>
    <!-- Class Title -->
    <div class="flex space-x-2 justify-left px-20">
      <h3
        class="text-2xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0"
      >
        Semester: {{ JSON.parse(course).semester }}
      </h3>
    </div>
    <!-- Semester and Professor Fields -->
    <div class="flex space-x-10 justify-left px-16">
      <!-- Professor -->
      <h3
        class="text-1xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0 px-4"
      >
        Professor:
      </h3>
      <div class="form-group mb-3 w-1/2">
        <input
          type="text"
          class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-800 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:border-blue-600 focus:outline-none"
          id="exampleInput7"
          placeholder="Professor"
          v-model="prof"
        />
      </div>
    </div>
    <div class="py-5"></div>

    <!-- Review Text -->
    <!-- Sample Review Gudied Questions -->
    <!-- Work -->
    <!-- What is the Workload-->
    <!-- Assignments Style -->
    <!-- Exams Style-->
    <!-- Outside of class time to dedicate (including studying)? -->

    <!-- Class/Lecture -->
    <!-- Teaching Style -->
    <!-- Teaching Effectiveness  -->
    <!-- Professor Availably  -->
    <!-- Grading Style  -->

    <!-- Feedback to teacher-->
    <h3
      class="text-2xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0 px-20"
    >
      General Course Information
    </h3>
    <div class="flex space-x-2 justify-left px-20">
      <div class="form-group mb-3 w-full">
        <h3
          class="text-1xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0"
        >
          Teaching Style:
        </h3>
        <textarea
          required
          class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-800 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:border-blue-600 focus:outline-none"
          id="exampleFormControlTextarea13"
          rows="3"
          placeholder="Review"

          v-model="teachStyle"
          
        ></textarea>
      </div>
    </div>
    <div class="flex space-x-2 justify-left px-20">
      <div class="form-group mb-3 w-full">
        <h3
          class="text-1xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0"
        >
          Grading Style:
        </h3>
        <textarea
          required
          class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-800 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:border-blue-600 focus:outline-none"
          id="exampleFormControlTextarea13"
          rows="3"
          placeholder="Review"
          v-model="gradeStyle"
        ></textarea>
      </div>
    </div>
    <div class="flex space-x-2 justify-left px-20">
      <div class="form-group mb-3 w-full">
        <h3
          class="text-1xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0"
        >
          Teacher Feedback:
        </h3>
        <textarea
          required
          class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-800 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:border-blue-600 focus:outline-none"
          id="exampleFormControlTextarea13"
          rows="3"
          placeholder="Review"
          v-model="teachFeedback"
        ></textarea>
      </div>
    </div>

    <div class="py-5"></div>

    <h3
      class="text-2xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0 px-20"
    >
      Workload and Assignment Information
    </h3>
    <div class="flex space-x-2 justify-left px-20">
      <div class="form-group mb-3 w-full">
        <h3
          class="text-1xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0"
        >
          Workload/Time Comitmment:
        </h3>
        <textarea
          required
          class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-800 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:border-blue-600 focus:outline-none"
          id="exampleFormControlTextarea13"
          rows="3"
          placeholder="Review"
          v-model="workload"
        ></textarea>
      </div>
    </div>
    <div class="flex space-x-2 justify-left px-20">
      <div class="form-group mb-3 w-full">
        <h3
          class="text-1xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0"
        >
          Assignment Style:
        </h3>
        <textarea
          required
          class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-800 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:border-blue-600 focus:outline-none"
          id="exampleFormControlTextarea13"
          rows="3"
          placeholder="Review"
          v-model="assignment"
        ></textarea>
      </div>
    </div>
    <div class="flex space-x-2 justify-left px-20">
      <div class="form-group mb-3 w-full">
        <h3
          class="text-1xl font-medium leading-tight text-gray-800 dark:text-gray-200 mb-3 mt-0"
        >
          Exam Style:
        </h3>
        <textarea
          required
          class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-800 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:border-blue-600 focus:outline-none"
          id="exampleFormControlTextarea13"
          rows="3"
          v-model="exam"
          placeholder="Review"
        ></textarea>
      </div>
    </div>

    <!-- Submit Button -->
    <!-- When clicked, triggers POST request to send a review to the DB -->
    <div class="flex space-x-2 justify-center w-full">
      <div class="p-4 ...">
        <button
          type="submit"
          class="w-full px-6 py-2.5 bg-blue-600 dark:bg-blue-700 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 dark:hover:bg-blue-900 hover:shadow-lg focus:bg-blue-700 dark:focus:bg-blue-900 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg peer-required:disable transition duration-150 ease-in-out"
          @click="submitReview"
        >
          Send
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import SelectMenu from "./SelectMenu.vue";
import axios from "axios";
import 'mosha-vue-toastify/dist/style.css';
import { createToast } from 'mosha-vue-toastify';




export default defineComponent({
  components: { SelectMenu },
  data() {
    return {
      prof: "",
      teachStyle: "",
      gradeStyle: "",
      teachFeedback: "",
      workload: "",
      assignment: "",
      exam: "",
      semesters: [
        {
            id: 1,
            name: 'Please Choose an Option',
        },
        {
            id: 2,
            name: 'Fall 2021',
        },
        {
            id: 3,
            name: 'Spring 2021',
        },
        {
            id: 4,
            name: 'Fall 2020',
        }
      ],
    };
  },
  props: {
    course: String, // passed as stringified Object, needs to be parsed
  },
  methods: {
    submitReview() {
      
      if (this.prof == "" || this.teachStyle  == ""|| this.gradeStyle == ""||
        this.teachFeedback == ""|| this.workload == ""|| this.assignment == ""|| this.exam == "") {
        createToast('Please Fill Out All Fields',
            {
            type: 'warning',
            transition: 'zoom',
            position: 'bottom-center',
            showIcon: true,
            });
      } else {
        axios.post(
          `http://127.0.0.1:8000/course/review/api/${JSON.parse(course).id}`,
          // `https://jhcourserevu-api-test.herokuapp.com/course/review/api/`,
          {
            "comments": {
              "Professor": this.prof,
              "Teaching Style": this.teachStyle,
              "Grading Style": this.gradeStyle,
              "Teacher Feedback": this.teachFeedback,
              "Workload": this.workload,
              "Assignment Style": this.assignment,
              "Exam Style": this.exam,
            },
            "course_id" : JSON.parse(this.course).id,
          })
            .then(function (response) {
              console.log(response);
              createToast('Review Successfully Sent',
              {
              type: 'success',
              transition: 'zoom',
              position: 'bottom-center',
              showIcon: true,
              });
              // console.log(this);
              // this.teachStyle  = "";
              // this.gradeStyle = "";
              // this.teachFeedback = "";
              // this.workload = "";
              // this.assignment = "";
              // this.exam = "";
            })
            .catch(function (error) {
              console.log(error);
              createToast('Review Could Not be Sent',
                {
                type: 'danger',
                transition: 'zoom',
                position: 'bottom-center',
                showIcon: true,
                });
              
              });
      }
      
    },
  },
});
</script>



