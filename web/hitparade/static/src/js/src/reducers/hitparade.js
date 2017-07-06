import * as HitParadeActionTypes from '../actiontypes/hitparade';
const svgShare = {
  	img: 'share.svg',
  	width: '15px',
  	height: '16px',
  	maxHeight: '16px',
  };
const svgContact = {
	 	img: 'copy.svg',
	  	width: '15px',
	  	height: '16px',
	  	maxHeight: '16px',
  } ;
const svgCart = {
  		img: 'cart.png',
  		width: '20px',
  		height: '20px',
  		maxHeight: '20px',
  };
const initialState = {
	imgRoot: '/static/dist/images/',
	cart: [{}],
	playersInCart: 4,
	heroImage: 'Hero.png',
	heroImageMobile: 'heroImageMobile.svg',
	showModal: false,
	showDrawer: false,
	svgs: {
		svgContact: svgContact,
		svgShare: svgShare,
		svgCart: svgCart,
	},
};
export default function HitParade(state=initialState, action) {
	switch(action.type) {
	case HitParadeActionTypes.NAV_SELECT_PLAYERS:
		return {
			...state,
		};
	case HitParadeActionTypes.NAV_FAQ:
		return {
			...state,
		};
	case HitParadeActionTypes.NAV_CONTACT:
		return {
			...state,
		};
	case HitParadeActionTypes.TERMS_OF_USE:
		return {
			...state,
		};
	case HitParadeActionTypes.NAV_CLOSE_MODAL:
		return {
			...state,
			showModal: false,
		};
	case HitParadeActionTypes.NAV_SIGNUP:
		return {
			...state,
			showModal: true,
			modalData: 'signUp'
		};
	case HitParadeActionTypes.NAV_LOGIN:
		return {
			...state,
		};
	case HitParadeActionTypes.NAV_CONTACT:
		return {
			...state,
		};
	case HitParadeActionTypes.SELECT_PLAYER:
		state.playersInCart += 1;
		return state;
	case HitParadeActionTypes.REMOVE_PLAYER:
		return {
			...state,
			playersInCart: (state.playersInCart-1),
		};
	case HitParadeActionTypes.CART:
		return {
			...state,
		};
	case HitParadeActionTypes.NAV_SHARE:
		return {
			...state,
			showModal: true,
			modalData: 'share'
		}
	case HitParadeActionTypes.NAV_PRIVACY_STATEMENT:
		return {
			...state,
		}
	case HitParadeActionTypes.TOGGLE_HAMBRUGER:
		return {
			...state,
			showDrawer: !state.showDrawer
		}
	default:
		return state;
	}
}