<template>
  <div
    class="from-emerald-500 bg-gradient-to-tr to-teal-300 min-h-screen flex justify-center items-center"
  >
    <!-- card -->
    <div class="bg-white divide-y rounded-lg">
      <!-- up -->
      <div class="p-8">
        <h1
          class="text-emerald-400 text-center text-2xl font-bold tracking-wider"
        >
          BMI 計算器
        </h1>
        <div>
          <label class="mt-6 inline-block mb-1 text-gray-400">身高</label>
          <div
            class="flex items-center px-4 py-1.5 border border-emerald-300 rounded-lg"
          >
            <input
              type="number"
              class="block w-full mr-1.5 focus:outline-none"
              v-model="height"
            />
            <span class="shrink-0 text-emerald-500 text-sm select-none"
              >公分</span
            >
          </div>
        </div>
        <div>
          <label class="mt-6 inline-block mb-1 text-gray-400">體重</label>
          <div
            class="flex items-center px-4 py-1.5 border border-emerald-300 rounded-lg"
          >
            <input
              type="number"
              class="block w-full mr-1.5 focus:outline-none"
              v-model="weight"
            />
            <span class="shrink-0 text-emerald-500 text-sm select-none"
              >公斤</span
            >
          </div>
        </div>

        <div class="mt-6 text-center">
          <span class="text-gray-400"> BMI </span>
          <span class="text-2xl"> {{ bmi }} </span>
        </div>

        <div
          class="mt-6 py-1.5 bg-amber-200 text-amber-600 text-center text-lg font-bold ring-1 ring-amber-500/30 rounded-md shadow-lg shadow-amber-200"
          v-if="result === '過輕'"
        >
          你的體重是「過輕」
        </div>
        <div
          class="mt-6 py-1.5 bg-green-200 text-green-600 text-center text-lg font-bold ring-1 ring-green-500/30 rounded-md shadow-lg shadow-green-200"
          v-if="result === '正常'"
        >
          你的體重是「正常」
        </div>
        <div
          class="mt-6 py-1.5 bg-amber-200 text-amber-600 text-center text-lg font-bold ring-1 ring-amber-500/30 rounded-md shadow-lg shadow-amber-200"
          v-if="result === '過重'"
        >
          你的體重是「過重」
        </div>
        <div
          class="mt-6 py-1.5 bg-orange-200 text-orange-600 text-center text-lg font-bold ring-1 ring-orange-500/30 rounded-md shadow-lg shadow-orange-200"
          v-if="result === '輕度肥胖'"
        >
          你的體重是「輕度肥胖」
        </div>
        <div
          class="mt-6 py-1.5 bg-red-200 text-red-500 text-center text-lg font-bold ring-1 ring-red-500/30 rounded-md shadow-lg shadow-red-200"
          v-if="result === '中度肥胖'"
        >
          你的體重是「中度肥胖」
        </div>
        <div
          class="mt-6 py-1.5 bg-red-200 text-red-600 text-center text-lg font-bold ring-1 ring-red-500/30 rounded-md shadow-lg shadow-red-200"
          v-if="result === '重度肥胖'"
        >
          你的體重是「重度肥胖」
        </div>
      </div>

      <!-- down -->
      <div class="p-8">
        <ul class="space-y-1">
          <li class="flex text-amber-400">
            <div class="w-24 font-bold">體重過輕</div>
            <div>BMI &lt; 18.5</div>
          </li>
          <li class="flex text-green-400">
            <div class="w-24 font-bold">正常範圍</div>
            <div>18.5 ≤ BMI &lt; 24</div>
          </li>
          <li class="flex text-amber-400">
            <div class="w-24 font-bold">過重</div>
            <div>24 ≤ BMI &lt; 27</div>
          </li>
          <li class="flex text-orange-400">
            <div class="w-24 font-bold">輕度肥胖</div>
            <div>27 ≤ BMI &lt; 30</div>
          </li>
          <li class="flex text-red-400">
            <div class="w-24 font-bold">中度肥胖</div>
            <div>30 ≤ BMI &lt; 35</div>
          </li>
          <li class="flex text-red-500">
            <div class="w-24 font-bold">重度肥胖</div>
            <div>35 ≤ BMI</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      height: "",
      weight: "",
    };
  },
  watch: {},
  computed: {
    bmi() {
      if (!this.height || !this.weight) {
        return "";
      }
      const bmiFloat =
        this.weight / ((this.height / 100) * (this.height / 100));
      return bmiFloat.toFixed(1);
    },
    result() {
      const bmi = Number(this.bmi);
      if (bmi == 0) {
        return "";
      } else if (bmi < 18.5) {
        return "過輕";
      } else if (18.5 <= bmi && bmi < 24) {
        return "正常";
      } else if (24 <= bmi && bmi < 27) {
        return "過重";
      } else if (27 <= bmi && bmi < 30) {
        return "輕度肥胖";
      } else if (30 <= bmi && bmi < 35) {
        return "中度肥胖";
      } else if (35 <= bmi) {
        return "重度肥胖";
      }
      return "";
    },
  },
  methods: {},
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
