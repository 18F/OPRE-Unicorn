import { useSelector, useDispatch } from "react-redux";
import { StepIndicator } from "../../components/UI/StepIndicator/StepIndicator";
import { ProcurementShopSelect } from "../budgetLines/ProcurementShopSelect";
import { AgreementTypeSelect } from "./AgreementTypeSelect";
import { ProductServiceCodeSelect } from "./ProductServiceCodeSelect";
import {
    setProcurementShopsList,
    setSelectedProcurementShop,
    setAgreementTitle,
    setAgreementDescription,
    setAgreementProductServiceCode,
    setAgreementReason,
    setAgreementIncumbent,
    setAgreementProjectOfficer,
    setAgreementTeamMembers,
    setAgreementNotes,
} from "./createAgreementSlice";

export const StepCreateAgreement = ({ goBack, goToNext, wizardSteps }) => {
    const dispatch = useDispatch();
    const agreementTitle = useSelector((state) => state.createAgreement.agreement.name);
    const agreementDescription = useSelector((state) => state.createAgreement.agreement.description);
    const agreementNotes = useSelector((state) => state.createAgreement.agreement.notes);

    // const handleEditForm = (e) => {
    //     e.preventDefault();
    //     dispatch(
    //         setEditBudgetLineAdded({
    //             id: budgetLinesAdded[budgetLineBeingEdited].id,
    //             line_description: enteredDescription,
    //             comments: enteredComments,
    //             can_id: selectedCan?.id,
    //             can_number: selectedCan?.number,
    //             agreement_id: selectedAgreement?.id,
    //             amount: enteredAmount,
    //             date_needed: `${enteredYear}-${enteredMonth}-${enteredDay}`,
    //             psc_fee_amount: selectedProcurementShop?.fee,
    //         })
    //     );
    // };

    // const handleSubmitForm = (e) => {
    //     e.preventDefault();
    //     dispatch(
    //         setBudgetLineAdded([
    //             ...budgetLinesAdded,
    //             {
    //                 id: crypto.getRandomValues(new Uint32Array(1))[0],
    //                 line_description: enteredDescription,
    //                 comments: enteredComments,
    //                 can_id: selectedCan?.id,
    //                 can_number: selectedCan?.number,
    //                 agreement_id: selectedAgreement?.id,
    //                 amount: enteredAmount,
    //                 status: "DRAFT",
    //                 date_needed: `${enteredYear}-${enteredMonth}-${enteredDay}`,
    //                 psc_fee_amount: selectedProcurementShop?.fee,
    //                 created_on: new Date().toISOString(),
    //             },
    //         ])
    //     );

    //     //reset form
    //     dispatch(setEnteredDescription(""));
    //     dispatch(setEnteredAmount(null));
    //     dispatch(setSelectedCan({}));
    //     dispatch(setEnteredMonth(""));
    //     dispatch(setEnteredDay(""));
    //     dispatch(setEnteredYear(""));
    //     dispatch(setEnteredComments(""));
    //     alert("Budget Line Added");
    // };

    return (
        <>
            <h2 className="font-sans-lg">Create New Budget Line</h2>
            <p>Step Two: Creating a new Agreement</p>
            <StepIndicator steps={wizardSteps} currentStep={2} />
            <h2 className="font-sans-md">Select the Agreement Type</h2>
            <p>Select the type of agreement you would like to create.</p>
            <AgreementTypeSelect />

            <h2 className="font-sans-md">Agreement Details</h2>
            <label className="usa-label" htmlFor="bl-description">
                Agreement Title
            </label>
            <input
                className="usa-input"
                id="bl-description"
                name="bl-description"
                type="text"
                value={agreementTitle || ""}
                onChange={(e) => dispatch(setAgreementTitle(e.target.value))}
                required
            />

            <label className="usa-label" htmlFor="agreement-description">
                Description
            </label>
            <input
                className="usa-input"
                id="agreement-description"
                name="agreement-description"
                type="text"
                value={agreementDescription || ""}
                onChange={(e) => dispatch(setAgreementDescription(e.target.vaue))}
            />

            <ProductServiceCodeSelect />

            <h2 className="font-sans-md">Procurement Shop</h2>
            <p>
                Select the Procurement Shop, and the fee rates will be populated in the table below. If this is an
                active agreement, it will default to the procurement shop currently being used.
            </p>
            <ProcurementShopSelect />

            <h2 className="font-sans-md">Reason for Agreement</h2>
            {/* <AgreementReasonSelect /> */}
            {/* <IncumbentSelect /> */}
            <select />
            <select />

            <h2 className="font-sans-md">Points of Contact</h2>
            {/* <ProjectOfficerSelect /> */}
            {/* <TeamMembersSelect /> */}
            <label>Team Members Added</label>
            {/* <TeamMembersPreview /> */}

            <h2 className="font-sans-md">Notes</h2>
            <input
                className="usa-input"
                id="agreement-notes"
                name="agreement-notes"
                type="text"
                value={agreementNotes || ""}
                onChange={(e) => dispatch(setAgreementNotes(e.target.vaue))}
            />
        </>
    );
};
