<template>
  <div class="Home">
    <div class="container mt-2">
      <div v-for="(question, index) in questions" :key=index>
        <p class="mb-0">
          Posted By:
          <span class="question-author">{{ question.author }}</span>
        </p>
        <h2>
          <router-link
            :to="{ name: 'Question', params: { slug: question.slug } }"
            class="question-link"
            >{{ question.content }}
          </router-link>
        </h2>
        <p>Answers: {{ question.answers_count }}</p>
      </div>
      <div class="my-4">
        <p v-show="loadingQuestions">...loading...</p>
        <button
          v-show="next"
          @click="getQuestions"
          class="btn btn-sm, btn-outline-success"
        >
          load more
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "Home",
  data() {
    return {
      questions: [],
      next: null,
      loadingQuestions: false,
    };
  },
  methods: {
    // use lifecycle hooks
    getQuestions() {
      let endpoint = "api/questions/";
      if (this.next) {
        endpoint = this.next;
      }
      //console.log(endpoint);
      this.loadingQuestions = true;
      apiService(endpoint).then((data) => {
        this.questions.push(...data.results);
        this.questions.reverse();
        this.loadingQuestions = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
  },
  // computed:{
  //   reverseQuestion(){
  //     return this.questions.reverse();
  //   }
  // },
  created() {
    this.getQuestions();
    document.title = "MyQuora - Ask Anything!";
    //console.log(this.questions)
  },
};
</script>

<style scoped>
.question-author {
  font-weight: bold;
  color:rgb(56, 56, 129);
}
.question-link {
  font-weight: bold;
  color: black;
}
.question-link.hover {
  font-weight: bold;
  color: black;
}
</style>
