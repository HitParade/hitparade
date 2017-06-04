import * as HitParadeActionTypes from '../actiontypes/hitparade';


export const closeModal = () => {
  return {
    type: HitParadeActionTypes.NAV_CLOSE_MODAL,
  };
};
export const selectPlayer = (index) => {
  return {
    type: HitParadeActionTypes.SELECT_PLAYER,
    index
  };
};
export const removePlayer =  (index) => {
  return {
    type: HitParadeActionTypes.REMOVE_PLAYER,
    index
  };
};
export const navLogin =  () => {
  return {
    type: HitParadeActionTypes.NAV_LOGIN,
  };
};
export const navTermsOfUse =  () => {
  return {
    type: HitParadeActionTypes.TERMS_OF_USE,
  };
};
export const navSignup =  () => {
  return {
    type: HitParadeActionTypes.NAV_SIGNUP,
  };
};
export const cart =  () => {
  return {
    type: HitParadeActionTypes.CART,
  };
};
export const navShare =  () => {
  return {
    type: HitParadeActionTypes.NAV_SHARE,
  };
};
export const navPrivacyStatement =  () => {
  return {
    type: HitParadeActionTypes.NAV_PRIVACY_STATEMENT,
  };
};
export const navContact =  () => {
  return {
    type: HitParadeActionTypes.NAV_CONTACT,
  };
};
export const navFaq =  () => {
  return {
    type: HitParadeActionTypes.NAV_FAQ,
  };
};
export const navSelectPlayers =  () => {
  return {
    type: HitParadeActionTypes.NAV_SELECT_PLAYERS,
  };
};