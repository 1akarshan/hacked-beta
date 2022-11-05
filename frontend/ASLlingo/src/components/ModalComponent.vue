<template>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-button color="medium" @click="cancel">Cancel</ion-button>
        </ion-buttons>
        <ion-title>Modal</ion-title>
        <ion-buttons slot="end">
          <ion-button @click="confirm">Confirm</ion-button>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
        <p>{{id}}</p>
        <p>{{title}}</p>
        <p>{{question}}</p>
        <p>{{difficulty}}</p>
        <p>{{color}}</p>
        <p>{{JSON.stringify(videoInfo)}}</p>
        <ion-button @click="takeVideo" shape="circle">
            <ion-icon :md="icon.md" :ios="icon.ios"></ion-icon>
        </ion-button>
        
        
      
      
    </ion-content>
  </template>
  
  <script >
    import {
      IonContent,
      IonIcon,
      IonHeader,
      IonTitle,
      IonToolbar,
      IonButtons,
      IonButton,
      modalController,
    } from '@ionic/vue';
    import { defineComponent } from 'vue';
    import { cameraOutline  } from 'ionicons/icons';
    import {MediaCapture} from '@awesome-cordova-plugins/media-capture';
  import {Capacitor} from '@capacitor/core';
  import axios from 'axios';
    export default defineComponent({
      name: 'ModalVue',
      components: { IonContent, IonHeader, IonTitle, IonToolbar, IonButtons, IonButton,IonIcon },
      data() {
        return {
            videoInfo: {},
            icon: {
                md: cameraOutline,
                ios: cameraOutline
            }
        }
      },
      props: {
        id: {
          type: Number,
          default: null,
        },
        title: {
          type: String,
          default: null,
        },
        question: {
          type: String,
          default: null,
        },
        difficulty: {
          type: String,
          default: null,
        },
        color: {
          type: String,
          default: null,
        },
      },
      methods: {
        cancel() {
          return modalController.dismiss('cancel', this.videoInfo);
        },
        confirm() {
          return modalController.dismiss();
        },
        takeVideo: async function () {
        
        try {
          const options = {
            duration: 10,
            limit: 1,
            quality: 1
          };
          const result = await MediaCapture.captureVideo(options);
          this.videoInfo = result[0];
          // console.log("videoInfo", JSON.stringify(result[0]));
          const blob = await fetch(
            Capacitor.convertFileSrc(this.videoInfo.fullPath)
          ).then(r => r.blob());
          const formData = new FormData();
          formData.append("file", blob, this.videoInfo.name);
          // convert video blob to base64
          let reader = new FileReader();
          reader.readAsDataURL(blob);
          reader.onloadend = async function() {
            let base64data = reader.result;
            let trimmed = base64data.substring(base64data.indexOf(",") + 1);
           console.log(trimmed); // DEBUG
          axios({
            method: "post",
            url: "https://51d1-2620-101-c040-85c-d08b-6896-278c-74d5.ngrok.io/upload/",
            data: JSON.stringify({
              _data: trimmed
            }),
          headers: {
            "Content-Type": "application/json"
          }
          }).then((response) => {
            alert(response.status);
          });
          };
        } catch (error) {
            // NEVER PUT ALERT HERE
          console.log(error);
      }
    }
      },
    });
  </script>