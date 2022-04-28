<template>
  <!-- <div>名字: {{ name }}</div>
  <input
    type="text"
    :value="name"
    @input="(event) => (name = event.target.value)"
  />
  <input type="text" v-model="name" /> -->
  <!-- <div>
    技能
    <ul>
      <li v-for="(skill, index) in skills" :key="index">
        {{ index + " - " + skill }}
      </li>
    </ul>
  </div> -->
  <!-- <button v-on:click="count++">計數： {{ count }}</button> -->
  <!-- <button @click="count++">計數： {{ count }}</button> -->

  <div>
    <button @click="show = !show">切換</button>
    <Transition
      enter-active-class="transition duration-1000 ease"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition duration-1000 ease"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-if="show">
        losdfasdfiel jwej iowejflkwjof;jwefjwej flkjds f sdio
      </div>
    </Transition>
  </div>
  <!-- <input type="number" v-model.number="a"> +
  <input type="text" v-model.number="b"> =
  {{ result }} -->
  <!-- 1+2=
  <input type="text" v-model.number='ans' > -->
  <!-- <input type="text" ref="textInput" value="123"/> -->
</template>

<script>
export default {
  data() {
    return {
      isActive: true,
      name: "Joe",
      skills: ["a", "b", "c", "d", "e"],
      count: 0,
      show: false,
      a: "",
      b: "",
      ans: 0,
    };
  },
  watch: {
    ans(newV) {
      if (newV == 3) {
        alert("恭喜答對");
      }
    },
  },
  computed: {
    result() {
      return this.a + this.b;
    },
  },
  methods: {
    increment() {
      this.count += 1;
    },
    switch() {
      this.show = !this.show;
    },
  },
  created() {
    console.log("created");
    // console.log(this.$refs.textInput);
  },
  mounted() {
    console.log("mounted");
    // console.log(this.$refs.textInput);
    // console.log(this.$refs.textInput.value);
  },
  updated() {
    console.log("updated");
  },
};
</script>
