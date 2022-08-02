import { setCanList } from "./canListSlice";
import ApplicationContext from "../../../applicationContext/ApplicationContext";

export const getCanList = () => {
    return async (dispatch, getState) => {
        const responseData = await ApplicationContext.get().helpers().callBackend("/ops/cans", "get");
        dispatch(setCanList(responseData));
    };
};
