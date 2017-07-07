import {
	NAV_FAQ,
	TERMS_OF_USE,
	NAV_CLOSE_MODAL,
	NAV_SIGNUP,
	NAV_LOGIN,
	NAV_CONTACT,
	SELECT_PLAYER,
	REMOVE_PLAYER,
	NAV_SELECT_PLAYERS,
	CART,
	NAV_SHARE,
	NAV_PRIVACY_STATEMENT,
} from '../actiontypes/hitparade';

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
	svgs: {
		svgContact: svgContact,
		svgShare: svgShare,
		svgCart: svgCart,
	},
};
// export default function HitParade(state=initialState, action) {
// 	switch(action.type) {
// 	case HitParadeActionTypes.NAV_SELECT_PLAYERS:
// 		return {
// 			...state,
// 		};
// 	case HitParadeActionTypes.NAV_FAQ:
// 		return {
// 			...state,
// 		};
// 	case HitParadeActionTypes.NAV_CONTACT:
// 		return {
// 			...state,
// 		};
// 	case HitParadeActionTypes.TERMS_OF_USE:
// 		return {
// 			...state,
// 		};
// 	case HitParadeActionTypes.NAV_CLOSE_MODAL:
// 		return {
// 			...state,
// 			showModal: false,
// 		};
// 	case HitParadeActionTypes.NAV_SIGNUP:
// 		return {
// 			...state,
// 			showModal: true,
// 		};
// 	case HitParadeActionTypes.NAV_LOGIN:
// 		return {
// 			...state,
// 		};
// 	case HitParadeActionTypes.NAV_CONTACT:
// 		return {
// 			...state,
// 		};
// 	case HitParadeActionTypes.SELECT_PLAYER:
// 		state.playersInCart += 1;
// 		return state;
// 	case HitParadeActionTypes.REMOVE_PLAYER:
// 		return {
// 			...state,
// 			playersInCart: (state.playersInCart-1),
// 		};
// 	case HitParadeActionTypes.CART:
// 		return {
// 			...state,
// 		};
// 	case HitParadeActionTypes.NAV_SHARE:
// 		return {
// 			...state,
// 		}
// 	case HitParadeActionTypes.NAV_PRIVACY_STATEMENT:
// 		return {
// 			...state,
// 		}
// 	default:
// 		return state;
// 	}
// }


const HitParade = {
  state: initialState, 
  actions: {
	[NAV_CLOSE_MODAL]: (state, action) => {
		return {
			...state,
			showModal: false,
		};
	},
	[NAV_SIGNUP]: (state, action) => {
		return {
			...state,
			showModal: true,
			modalData: 'signUp'
		};
	},
	[SELECT_PLAYER]: (state, action) => {
		return {
			...state,
			playersInCart: state.playersInCart += 1
		}
	},
	[REMOVE_PLAYER]: (state, action) => {
		return {
			...state,
			playersInCart: (state.playersInCart-1),
		};

	},
	[NAV_LOGIN]: (state, action) => state,
	[NAV_SELECT_PLAYERS]: (staet, action) => state,
	[NAV_FAQ]: (state, action) => state,
	[NAV_CONTACT]: (state, action) => state,
	[TERMS_OF_USE]: (state, action) => state,
	[CART]: (state, action) => state,
	[NAV_SHARE]: (state, action) => {
		return {
			...state,
			showModal: true,
			modalData: 'share'
		}
	},
	[NAV_PRIVACY_STATEMENT]: (state, action) => state,
  }
};


export default HitParade;
