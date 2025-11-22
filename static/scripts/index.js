import {
  createScope,
  createTimeline,
  stagger,
  text,
  utils,
} from 'https://esm.sh/animejs';

console.log("hello")

createScope({
  root: '#subtle-highlight',
  defaults: { ease: 'out(3)', duration: 350, composition: 'blend' },
}).add((scope) => {

  const { root, methods } = scope;
  const { chars } = text.splitText('h1', { chars: true });

  utils.set(chars, { opacity: .5 });

  scope.add('onEnter', () => createTimeline().add(chars, { opacity: 1, textShadow: '0 0 30px rgba(255,255,255,.9)' }, stagger(12)));
  scope.add('onLeave', () => createTimeline().add(chars, { opacity: .5, textShadow: '0 0 0px rgba(255,255,255,0)' }, stagger(12)));

  root.addEventListener('pointerenter', methods.onEnter);
  root.addEventListener('pointerleave', methods.onLeave);

});