import React from "react";
import {
    useAddCanFundingBudgetsMutation,
    useUpdateCanFundingBudgetMutation,
    useAddCanFundingReceivedMutation
} from "../../../api/opsAPI.js";
import { getCurrentFiscalYear } from "../../../helpers/utils.js";
import useAlert from "../../../hooks/use-alert.hooks";
import suite from "./CanFundingSuite.js";
import classnames from "vest/classnames";
import { NO_DATA } from "../../../constants.js";
import { useSelector } from "react-redux";

/**
 * @typedef {import("../../../components/CANs/CANTypes").FundingReceived} FundingReceived
 */

/**
 * @description - Custom hook for the CAN Funding component.
 * @param {number} canId
 * @param {string} canNumber
 * @param {string} totalFunding
 * @param {number} fiscalYear
 * @param {boolean} isBudgetTeamMember
 * @param {boolean} isEditMode
 * @param {() => void} toggleEditMode
 * @param {string} receivedFunding
 * @param {FundingReceived[]} fundingReceived
 * @param {number} [currentFiscalYearFundingId] - The id of the current fiscal year funding. optional
 */
export default function useCanFunding(
    canId,
    canNumber,
    totalFunding,
    fiscalYear,
    isBudgetTeamMember,
    isEditMode,
    toggleEditMode,
    receivedFunding,
    fundingReceived,
    currentFiscalYearFundingId
) {
    const currentFiscalYear = getCurrentFiscalYear();
    const showButton = isBudgetTeamMember && fiscalYear === Number(currentFiscalYear) && !isEditMode;
    const [showModal, setShowModal] = React.useState(false);
    const [totalReceived, setTotalReceived] = React.useState(parseFloat(receivedFunding || "0"));
    const [enteredFundingReceived, setEnteredFundingReceived] = React.useState([...fundingReceived]);
    const [modalProps, setModalProps] = React.useState({
        heading: "",
        actionButtonText: "",
        secondaryButtonText: "",
        handleConfirm: () => {}
    });

    const [budgetForm, setBudgetForm] = React.useState({
        enteredAmount: "",
        submittedAmount: "",
        isSubmitted: false
    });

    const [fundingReceivedForm, setFundingReceivedForm] = React.useState({
        enteredAmount: "",
        submittedAmount: "",
        enteredNotes: "",
        submittedNotes: "",
        isSubmitted: false
    });

    const [addCanFundingBudget] = useAddCanFundingBudgetsMutation();
    const [updateCanFundingBudget] = useUpdateCanFundingBudgetMutation();
    const [addCanFundingReceived] = useAddCanFundingReceivedMutation();
    const { setAlert } = useAlert();
    const activeUserFullName = useSelector((state) => state.auth?.activeUser?.full_name) || "";

    React.useEffect(() => {
        setBudgetForm({ ...budgetForm, submittedAmount: totalFunding });
    }, [totalFunding]);

    React.useEffect(() => {
        setEnteredFundingReceived([...fundingReceived]);
    }, [fundingReceived]);

    const handleEnteredBudgetAmount = (value) => {
        const nextForm = {
            ...budgetForm,
            enteredAmount: value
        };
        setBudgetForm(nextForm);
    };

    const handleEnteredFundingReceivedAmount = (value) => {
        const nextForm = {
            ...fundingReceivedForm,
            enteredAmount: value
        };
        setFundingReceivedForm(nextForm);
    };

    const handleEnteredNotes = (value) => {
        const nextForm = {
            ...fundingReceivedForm,
            enteredNotes: value
        };
        setFundingReceivedForm(nextForm);
    };

    // Validation
    let res = suite.get();

    const cn = classnames(suite.get(), {
        invalid: "usa-form-group--error",
        valid: "success",
        warning: "warning"
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        const payload = {
            fiscal_year: fiscalYear,
            can_id: canId,
            budget: budgetForm.submittedAmount
        };
        const fundingPayload = {
            fiscal_year: fiscalYear,
            can_id: canId,
            funding: fundingReceivedForm.submittedAmount,
            notes: fundingReceivedForm.submittedNotes
        };

        const updateFunding = async () => {
            try {
                if (+payload.budget > 0) {
                    if (currentFiscalYearFundingId) {
                        // PATCH for existing CAN Funding
                        await updateCanFundingBudget({
                            id: currentFiscalYearFundingId,
                            data: payload
                        }).unwrap();
                        console.log("CAN Funding Updated");
                    } else {
                        // POST for new CAN Funding
                        await addCanFundingBudget({
                            data: payload
                        }).unwrap();
                        console.log("CAN Funding Added");
                    }
                }

                if (+fundingPayload.funding > 0) {
                    await addCanFundingReceived({
                        data: fundingPayload
                    }).unwrap();
                    console.log("Funding Received Updated");
                }

                setAlert({
                    type: "success",
                    heading: "CAN Funding Updated",
                    message: `The CAN ${canNumber} has been successfully updated.`
                });
            } catch (error) {
                console.error("Error Updating CAN", error);
                setAlert({
                    type: "error",
                    heading: "Error",
                    message: "An error occurred while updating the CAN.",
                    redirectUrl: "/error"
                });
            }
        };

        updateFunding();
        cleanUp();
    };

    const handleAddBudget = (e) => {
        e.preventDefault();

        const nextForm = {
            ...budgetForm,
            enteredAmount: "",
            submittedAmount: budgetForm.enteredAmount,
            isSubmitted: true
        };
        setBudgetForm(nextForm);
    };

    const handleAddFundingReceived = (e) => {
        e.preventDefault();

        // Update total received first using the functional update pattern
        setTotalReceived((currentTotal) => currentTotal + +fundingReceivedForm.enteredAmount);

        // update the table data
        const newFundingReceived = {
            id: NO_DATA,
            created_on: new Date().toISOString(),
            created_by_user: {
                full_name: activeUserFullName
            },
            notes: fundingReceivedForm.enteredNotes,
            funding: +fundingReceivedForm.enteredAmount,
            fiscal_year: fiscalYear
        };
        setEnteredFundingReceived([...enteredFundingReceived, newFundingReceived]);
        // Then update the form state
        const nextForm = {
            ...fundingReceivedForm,
            enteredAmount: "",
            submittedAmount: fundingReceivedForm.enteredAmount,
            enteredNotes: "",
            submittedNotes: fundingReceivedForm.enteredNotes,
            isSubmitted: true
        };
        setFundingReceivedForm(nextForm);
    };

    const handleCancel = () => {
        setShowModal(true);
        setModalProps({
            heading: "Are you sure you want to cancel editing? Your changes will not be saved.",
            actionButtonText: "Cancel Edits",
            secondaryButtonText: "Continue Editing",
            handleConfirm: () => {
                setTotalReceived(parseFloat(receivedFunding || "0"));
                cleanUp();
            }
        });
    };

    const cleanUp = () => {
        setEnteredFundingReceived([...fundingReceived]);
        setBudgetForm({ enteredAmount: "", submittedAmount: totalFunding, isSubmitted: false });
        setShowModal(false);
        const nextForm = { ...fundingReceivedForm, enteredAmount: "", enteredNotes: "" };
        setFundingReceivedForm(nextForm);
        toggleEditMode();
        setModalProps({
            heading: "",
            actionButtonText: "",
            secondaryButtonText: "",
            handleConfirm: () => {}
        });
        suite.reset();
    };

    const runValidate = (name, value) => {
        suite({ remainingAmount: +budgetForm.submittedAmount - totalReceived, ...{ [name]: value } }, name);
    };

    return {
        handleAddBudget,
        handleAddFundingReceived,
        handleCancel,
        handleSubmit,
        modalProps,
        runValidate,
        res,
        cn,
        setShowModal,
        showButton,
        showModal,
        budgetForm,
        handleEnteredBudgetAmount,
        fundingReceivedForm,
        handleEnteredFundingReceivedAmount,
        handleEnteredNotes,
        totalReceived,
        enteredFundingReceived
    };
}
