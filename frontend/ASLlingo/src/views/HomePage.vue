<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div class="box" id="container">
        <p style="line-height: 0px;color:white;margin: 0;margin-left:2rem; margin-top:3rem; font-size:5rem;">Quiz!</p>
        <p style="line-height: 0px;color:white;margin: 0;margin-left:3rem; margin-top:4.5rem; font-size:1.5rem;">Master the ASL!</p>
        <p style="line-height: 0px;color:white;margin: 0;margin-left:3rem; margin-top:2rem; font-size:1rem;">Answer the questions below.
          <span style="font-size:2rem">🧐</span></p>
        <div id="whiteSpace"></div>
        <div v-for="item in items" :key="item.id" style="">
        <ion-card @click="openModal(item.id, item.title, item.question, item.difficulty, item.color, item.optionset1, item.optionset2, item.link, item.answer)" >
          <ion-card-header>
            <ion-card-subtitle class="ion-padding-horizontal" style="margin:10px, 0, 10px, 0; padding: 10px, 0, 10px, 0">{{item.title}}</ion-card-subtitle>
            <ion-card-title class="ion-padding-horizontal" style="margin:10px, 0, 10px, 0; padding: 10px, 0, 10px, 0">{{item.question}}</ion-card-title>
            
          </ion-card-header>
          <ion-card-content>
            <ion-grid>
              <ion-row>
                <ion-col class="ion-padding-horizontal">
                  <ion-text :color="item.color">
                    <p><strong>{{item.difficulty}}</strong></p>
                  </ion-text>
                  
                </ion-col>
                <ion-col></ion-col>
                <ion-col class="ion-no-padding">
                  
                </ion-col>

              </ion-row>
            </ion-grid>
            
          </ion-card-content>
        </ion-card>
      </div>
      </div>
      <!-- create a card with a for loop -->
      



    </ion-content>
  </ion-page>
</template>

<script>
  import { IonContent, IonCardHeader, IonPage, IonText, IonCard, IonCardContent, IonCardTitle, IonCardSubtitle, modalController, IonGrid, IonRow,IonCol,} from '@ionic/vue';
  import Modal from '../components/ModalComponent.vue';
  import { defineComponent } from 'vue';
  export default defineComponent({
    name: 'HomePage',
    components: {
      IonPage,
      IonContent,
      IonCardHeader,
      IonCard,
      IonCardTitle,
      IonCardSubtitle,
      IonCardContent,
      IonGrid,
      IonRow,
      IonCol,
      IonText,
    },
    data() {
      return {
        items: [
          {
            id: 1, 
            title: 'Question 1', 
            difficulty: 'Hard', 
            question: 'This classifier describes types of airplanes and is also the sign for "I Love You!"',
            color: 'danger',
            link: "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/63143/heart-love-clipart-md.png",
            answer: {title: 'CL-ILY', link:'https://www.lifeprint.com/asl101/images-layout/cl-ily.gif'},
          },
            {id: 2,
            title: 'Question 2', 
            difficulty: 'Easy', 
            question: 'This classifier might be used to describe a stick or pencil, or to draw a circle in the air', 
            color: 'success',
            answer: {title: 'CL-1', link:"https://www.lifeprint.com/asl101/images-layout/cl-l.gif"}, 
            optionset1: [
              {title: 'Option 1', link:"https://www.lifeprint.com/asl101/images-layout/cl-ily.gif"},
              {title: 'Option 2', link:"https://www.lifeprint.com/asl101/images-layout/cl-l.gif"}],
              optionset2: [
                {title: 'Option 3', link: "https://www.lifeprint.com/asl101/images-layout/cl-o.gif"},
                {title: 'Option 4', link:"https://www.lifeprint.com/asl101/images-layout/cl-r.gif"}
              ]
            },
            {
              id: 3,
            title: 'Question 3', 
            difficulty: 'Easy', 
            question: 'This classifier describes motorized vehicles, or groups of three ', 
            color: 'success',
            answer: {title: 'CL-3', link: "https://www.lifeprint.com/asl101/images-layout/cl-3.gif"},
            optionset1: [
              {title: 'Option 1', link:"https://www.lifeprint.com/asl101/images-layout/cl-c-cupped.gif"},
              {title: 'Option 2', link:"https://www.lifeprint.com/asl101/images-layout/cl-l.gif"}],
              optionset2: [
                {title: 'Option 3', link: "https://www.lifeprint.com/asl101/images-layout/cl-3.gif"},
                {title: 'Option 4', link:"https://www.lifeprint.com/asl101/images-layout/cl-ily.gif"}
              ]
            },
            {
              id: 4,
              title: 'Question 4', 
              difficulty: 'Hard', 
              answer: {title: 'CL-3C', link: "https://www.lifeprint.com/asl101/images-layout/cl-3-claw.gif"},
              question: 'This classifier describes a method of gripping objects using three fingers', 
              color: 'danger',
              link: "https://i.pinimg.com/originals/95/dc/95/95dc950425ac3dee2feca2f506194a17.png",
          },
          {
            id: 5,
            title: 'Question 5', 
            difficulty: 'Easy', 
            answer: {title: 'CL-4', link: "https://www.lifeprint.com/asl101/images-layout/cl-4.gif"},
            question: 'This classifier might be used to describe people standing in line, especially four people ', 
            color: 'success',
            optionset1: [
              {title: 'Option 1', link:"https://www.lifeprint.com/asl101/images-layout/cl-a.gif"},
              {title: 'Option 2', link:"https://www.lifeprint.com/asl101/images-layout/cl-4.gif"}], // ans
            optionset2: [
              {title: 'Option 3', link:"https://www.lifeprint.com/asl101/images-layout/cl-3.gif"},
              {title: 'Option 4', link:"https://www.lifeprint.com/asl101/images-layout/cl-b.gif"}
            ]

            
          },
          {
            id: 6,
            title: 'Question 6', 
            difficulty: 'Hard', 
            answer: {title: 'CL-5', link: "https://www.lifeprint.com/asl101/images-layout/cl-5.gif"},
            question: 'This classifier describes large flat objects, stiff and straight hair, flames, and more', 
            color: 'danger',
            link:"https://www.kindpng.com/picc/m/660-6604986_flaming-fire-png-image-animated-transparent-background-fire.png"
          },
          {id: 7,
          title: 'Question 7',
          answer: {title: 'CL-5C', link: "https://www.lifeprint.com/asl101/images-layout/cl-5-claw.gif"},
          difficulty: 'Hard', 
          question: 'This classifier might be used to describe large piles, curvy or wavy hair, and jaggedness ', 
          color: 'danger',
          link:"https://www.pngall.com/wp-content/uploads/12/Rich.png",
          },
          {id: 8,
          title: 'Question 8', 
          difficulty: 'Easy', 
          answer: {title: 'CL-A', link: "https://www.lifeprint.com/asl101/images-layout/cl-a.gif"},
          question: 'This classifier describes relative positioning to objects, for example, to say, “catch up!”', 
          color: 'success',
          optionset1: [
              {title: 'Option 1', link:"https://www.lifeprint.com/asl101/images-layout/cl-a.gif"}, // ANS
              {title: 'Option 2', link:"https://www.lifeprint.com/asl101/images-layout/cl-c-modified.gif"}],
            optionset2: [
              {title: 'Option 3', link:"https://www.lifeprint.com/asl101/images-layout/cl-f.gif"},
              {title: 'Option 4', link:"https://www.lifeprint.com/asl101/images-layout/cl-h-bent.gif"}
            ]
        },
        {
          id: 9,
          title: 'Question 9', 
          difficulty: 'Easy', 
          answer: {title: 'CL-BB', link: "https://www.lifeprint.com/asl101/images-layout/cl-b-bent.jpg"},
          question: 'This classifier might be used to describe a long stretch of road, or a shelf', 
          color: 'success',
          optionset1: [
              {title: 'Option 1', link:"https://www.lifeprint.com/asl101/images-layout/cl-5-claw.gif"},
              {title: 'Option 2', link:"https://www.lifeprint.com/asl101/images-layout/cl-1.gif"}],
            optionset2: [
              {title: 'Option 3', link:"https://www.lifeprint.com/asl101/images-layout/cl-3-claw.gif"},
              {title: 'Option 4', link:"https://www.lifeprint.com/asl101/images-layout/cl-b-bent.jpg"}
            ]
        },
          {
            id: 10,
            title: 'Question 10', 
            difficulty: 'Easy', 
            answer: {title: 'CL-CIT', link: "https://www.lifeprint.com/asl101/images-layout/cl-c-modified.gif"},
            question: 'This classifier describes small objects and demonstrates the holding of a small object', 
            color: 'success',
            optionset1: [
              {title: 'Option 1', link:"https://www.lifeprint.com/asl101/images-layout/cl-h-bent.gif"},
              {title: 'Option 2', link: "https://www.lifeprint.com/asl101/images-layout/cl-c-modified.gif"}],
            optionset2: [
              {title: 'Option 3', link:"https://www.lifeprint.com/asl101/images-layout/cl-g.gif"},
              {title: 'Option 4', link:"https://www.lifeprint.com/asl101/images-layout/cl-claw.gif"}
            ]
          }
        ]
      }
    },
    methods: {
      async openModal(id, title, question, difficulty, color, optionset1, optionset2, link, answer) {
        const modal = await modalController.create({
          component: Modal,
          componentProps: {
            id : id,
            title : title,
            question :  question,
            difficulty : difficulty,
            color : color,
            optionset1 : optionset1,
            optionset2 : optionset2,
            answer : answer,
            link : link
          }
        });
      modal.present();
      // const { data, role } = await modal.onWillDismiss();
      // alert(JSON.stringify(role)) IDEA: use this to get the data back from the modal and display something then
      // console.log(data)
      
      }
    }
  })
</script>

<style scoped>
ion-content{ 
  font-family: 'Ubuntu', sans-serif;
  font-weight: 900;
  
}
#whiteSpace{
  height: 5rem;
}
.box {
  width:100vw;
  height:40rem;
  display:inline-block;
  padding-top:10px;
  background:radial-gradient(100% 35% at top,#ff7454 99%,transparent 100%);
}
ion-thumbnail {
  --size: 50px;
  --border-radius: 14px;
}
ion-card{
  margin: 25px auto;
    display: flex;
    flex-direction: column;
    width: 90% !important;
    border-radius: 10px;
    background: #f8f4f4;
  }
  
</style>