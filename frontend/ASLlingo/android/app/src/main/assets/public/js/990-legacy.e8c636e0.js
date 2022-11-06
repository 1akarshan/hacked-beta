"use strict";(self["webpackChunkASLlingo"]=self["webpackChunkASLlingo"]||[]).push([[990],{8990:(t,e,n)=>{n.r(e),n.d(e,{createSwipeBackGesture:()=>s});var r=n(6587),i=n(545),o=n(6515);
/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
const s=(t,e,n,s,a)=>{const c=t.ownerDocument.defaultView,l=(0,i.i)(t),h=t=>{const e=50,{startX:n}=t;return l?n>=c.innerWidth-e:n<=e},u=t=>l?-t.deltaX:t.deltaX,d=t=>l?-t.velocityX:t.velocityX,k=t=>h(t)&&e(),w=t=>{const e=u(t),n=e/c.innerWidth;s(n)},g=t=>{const e=u(t),n=c.innerWidth,i=e/n,o=d(t),s=n/2,l=o>=0&&(o>.2||e>s),h=l?1-i:i,k=h*n;let w=0;if(k>5){const t=k/Math.abs(o);w=Math.min(t,540)}a(l,i<=0?.01:(0,r.h)(0,i,.9999),w)};return(0,o.A)({el:t,gestureName:"goback-swipe",gesturePriority:40,threshold:10,canStart:k,onStart:n,onMove:w,onEnd:g})}}}]);
//# sourceMappingURL=990-legacy.e8c636e0.js.map