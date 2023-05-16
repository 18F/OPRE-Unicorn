import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { setAgreementReasonsList, setSelectedAgreementReason, setAgreementIncumbent } from "./createAgreementSlice";
import { getAgreementReasons } from "../../api/getAgreements";
import {convertCodeForDisplay} from "../../helpers/utils";

export const AgreementReasonSelect = () => {
    const dispatch = useDispatch();
    const agreementReasons = useSelector((state) => state.createAgreement.agreement_reasons_list);
    const selectedAgreementReason = useSelector((state) => state.createAgreement.agreement.selected_agreement_reason);

    // On component load, get AgreementReasons from API, and set returned list in State
    useEffect(() => {
        const getAgreementReasonsAndSetState = async () => {
            dispatch(setAgreementReasonsList(await getAgreementReasons()));
        };

        getAgreementReasonsAndSetState().catch(console.error);

        return () => {
            dispatch(setAgreementReasonsList([]));
        };
    }, [dispatch]);

    const onChangeAgreementReasonSelection = (agreementReason) => {
        if (agreementReason === "0") {
            dispatch(setSelectedAgreementReason(null));
            dispatch(setAgreementIncumbent(null));
            return;
        }
        if (agreementReason === "NEW_REQ") {
            dispatch(setAgreementIncumbent(null));
        }

        dispatch(setSelectedAgreementReason(agreementReason));
    };

    return (
        <fieldset className="usa-fieldset">
            <label className="usa-label margin-top-0" htmlFor="reason-for-agreement-select">
                Reason for Agreement
            </label>
            <div className="display-flex flex-align-center margin-top-1">
                <select
                    className="usa-select margin-top-0 width-card-lg"
                    name="reason-for-agreement-select"
                    id="reason-for-agreement-select"
                    onChange={(e) => onChangeAgreementReasonSelection(e.target.value || 0)}
                    value={selectedAgreementReason || ""}
                    required
                >
                    <option value={0}>- Select Agreement Reason -</option>
                    {agreementReasons.map((reason, index) => (
                        <option key={index + 1} value={reason}>
                            {convertCodeForDisplay('AgreementReason', reason)}
                        </option>
                    ))}
                </select>
            </div>
        </fieldset>
    );
};

export default AgreementReasonSelect;
