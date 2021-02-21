<template>
  <v-container class="cards-container" :style="styles">
    <v-row>
      <v-col v-for="(card, index) in cards" :key="index" cols="4">
        <v-card class="cards-container__card">
          <base-loading v-if="isLoading"></base-loading>
          <img v-else class="image--style" :src="card.path" :alt="`ic-${card.value}`"/>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-btn @click="sendRequest" elevation="2">Begin the Game</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import BaseLoading from './BaseLoading.vue';

export default {
  name: 'the-main-game',
  components: {
    BaseLoading,
  },
  emits: ['on-begin-game'],
  props: {
    cards: {
      type: Array,
      required: true,
    },
    isLoading: {
      type: Boolean,
      default: false,
    }
  },
  computed: {
    styles() {
      return {
        '--margin-val': `${window.innerHeight / 4}px`,
      }
    }
  },
  methods: {
    sendRequest() {
      this.$emit('on-begin-game');
    },
  },
}
</script>

<style scoped>
/* Override default vuetify val */
@media (min-width: 960px) {
  .container {
    max-width: 100%;
  }
}
.cards-container {
  margin: 0;
  padding: 0 3em;
  width: 100%;
  padding-top: var(--margin-val);
}
.cards-container__card {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 10em;
}
.image--style {
  height: 5em;
  width: 5em;
}
</style>
