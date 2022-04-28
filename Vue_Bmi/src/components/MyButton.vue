<template>
  <button @click="$emit('my-event')">請戳我</button>
</template >

  <script>
    export default {
      emits: ["my-event"],
};
  </script>
