// options api

<template>
  <div>
    <!-- <Card name="name"></Card>
    <Card name="123"></Card> -->

    <MyButton @my-event="onMyEvent" />
  </div>
</template>

<script>
// import Card from './components/Card.vue';
import MyButton from './components/MyButton.vue';

export default {
  components: {
    // Card,
    MyButton
  },
  data() {},
  watch: {},
  computed: {},
  methods: {
    onMyEvent() {
      console.log("觸發")
    }
  },
  beforeCreate() {},
  created() {},
  beforeMount() {},
  mounted() {},
  beforeUpdate() {},
  updated() {},
  beforeUnmount() {},
  unmounted() {},
};
</script>
