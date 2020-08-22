<template>
  <div class="single-question mt-2">
    <div v-if="question" class="container">
      <h1>{{ question.content }}</h1>
      <QuestionActions
        v-if="isQuestionAuthor"
        :slug="question.slug"
      />
      <p class="mb-0">
        Posted By:
        <span class="author">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
      <hr />
      <div v-if="userHasAnswered">
        <p class="answer-added">Thanks for writing an answer!</p>
      </div>
      <div v-else-if="showForm">
        <form class="card" @submit.prevent="onSubmit">
          <div class="card-header px3">
            Answer the question
          </div>
          <div class="card-block">
            <textarea
              v-model="newAnswerBody"
              class="form-control"
              placeholder="Share your knowledge with the world"
              rows="5"
            ></textarea>
          </div>
          <div class="card-footer px3">
            <button type="submit" class="btn btn-sm btn-outline-success">
              Submit
            </button>
          </div>
        </form>
        <p v-if="error" class="error mt2">{{ error }}</p>
      </div>
      <div v-else>
        <button class="btn btn-sm btn-success" @click="showForm = true">
          Answer this question
        </button>
      </div>
    </div>
    <div v-else>
      <h1 id="notfound">404 - Question Not Found </h1>
    </div>
    <div v-if="question" class="container">
      <AnswerComponent
        v-for="(answer, index) in answers"
        :answer="answer"
				:requestUser="requestUser"
        :key="index"
				@delete-answer="deleteAnswer"
      />
      <div class="my-4">
        <p v-show="loadingAnswers">...loading...</p>
        <button
          v-show="next"
          @click="getQuestionAnswers"
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
import AnswerComponent from "@/components/Answer.vue";
import QuestionActions from "@/components/QuestionActions.vue";
export default {
  name: "Question",
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  components: {
    AnswerComponent,
    QuestionActions,
  },
  data() {
    return {
      question: {},
      answers: [],
      newAnswerBody: null,
      error: null,
      userHasAnswered: false,
      showForm: false,
      next: null,
			loadingAnswers: false,
			requestUser: null,
    };
  },
  computed: {
        isQuestionAuthor() {
            return this.question.author === this.requestUser;
        }
    },
  methods: {
    setPageTitle(title) {
      document.title = title;
		},
		setRequestUser() {
			this.requestUser = window.localStorage.getItem("username");
		},
    getQuestionData() {
      // get the details of a question instance from the REST API
      let endpoint = `/api/questions/${this.slug}/`;
      apiService(endpoint).then((data) => {
        if (data){
        this.question = data;
        this.userHasAnswered = data.user_has_answered;
        this.setPageTitle(data.content);
        }else{
          this.question = null;
          this.setPageTitle("404 - Page Not Found");
         
        }

      });
    },
    getQuestionAnswers() {
			let endpoint = `/api/questions/${this.slug}/answers/`;
			if (this.next) {
        endpoint = this.next;
			}
      this.loadingAnswers = true;
      apiService(endpoint).then((data) => {
        this.answers.push(...data.results);
        this.loadingAnswers = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
    onSubmit() {
      if (this.newAnswerBody) {
        let endpoint = `/api/questions/${this.slug}/answer/`;
        apiService(endpoint, "POST", { body: this.newAnswerBody }).this(
          (data) => {
            this.answers.unshift(data);
          }
        );
        this.newAnswerBody = null;
        this.showForm = false;
        this.userHasAnswered = true;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "Cannot send an empty answer!";
      }
		},
		async deleteAnswer(answer) {
			let endpoint=`/api/answers/${answer.id}/`;
			try{
				await apiService(endpoint, "DELETE");
				this.$delete(this.answers, this.answers.indexOf(answer));
				this.userHasAnswered = false;
			}
			catch(err){
				console.log(err);
			}
		}
  },
  created() {
    this.getQuestionData();
		this.getQuestionAnswers();
		this.setRequestUser();
  },
};
</script>

<style scoped>
.author {
  font-weight: bold;
  color: black;
}
.answer-added {
  font-weight: bold;
  color: green;
}
.error {
  font-weight: bold;
  color: red;
}
</style>
