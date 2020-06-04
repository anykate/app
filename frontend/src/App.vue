<template>
  <div id="app">
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input
          type="text"
          class="form-control col-sm-auto m-1"
          placeholder="Name"
          v-model="student.name"
        />
        <input
          type="text"
          class="form-control col-sm-3 m-1"
          placeholder="Course"
          v-model="student.course"
        />
        <input
          type="text"
          class="form-control col-sm-3 m-1"
          placeholder="Rating"
          v-model="student.rating"
        />
        <button class="btn btn-sm btn-outline-success col-sm-3 m-1">
          Submit
        </button>
      </div>
    </form>

    <!-- table.table>thead>th{Name}+th{Course}+th{Rating}^tbody>tr>td*3 -->
    <table class="table">
      <thead>
        <th>Name</th>
        <th>Course</th>
        <th>Rating</th>
        <th>Action</th>
      </thead>
      <tbody>
        <tr
          v-for="student in students"
          :key="student.id"
          @dblclick="$data.student = student"
        >
          <td>{{ student.name }}</td>
          <td>{{ student.course }}</td>
          <td>{{ student.rating }}</td>
          <td>
            <button
              class="btn btn-outline-danger btn-sm mx-1"
              @click="deleteStudent(student)"
            >
              x
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      student: {},
      students: [],
    };
  },
  async created() {
    await this.getStudents();
  },
  methods: {
    submitForm() {
      if (this.student.id === undefined) {
        this.createStudent();
      } else {
        this.editStudent();
      }
    },
    async getStudents() {
      let response = await fetch("http://localhost:8000/students/");
      this.students = await response.json();
    },
    async createStudent() {
      await this.getStudents();
      await fetch("http://localhost:8000/students/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.student),
      });
      await this.getStudents();
      this.student = {}; // Clear form
    },
    async editStudent() {
      await this.getStudents();
      await fetch(`http://localhost:8000/students/${this.student.id}/`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.student),
      });
      await this.getStudents();
      this.student = {}; // Clear form
    },
    async deleteStudent(student) {
      await this.getStudents();
      await fetch(`http://localhost:8000/students/${student.id}/`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.student),
      });
      await this.getStudents();
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
