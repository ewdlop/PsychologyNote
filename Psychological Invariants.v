Inductive State : Type :=
  | Neutral
  | Positive
  | Negative.

Inductive Action : Type :=
  | Give
  | Take
  | Ignore.

Definition utility (s : State) : nat :=
  match s with
  | Neutral => 0
  | Positive => 10
  | Negative => -15
  end.

Lemma loss_aversion :
  forall s1 s2 : State,
    utility s2 < 0 -> (* Negative state *)
    utility s2 - utility s1 < utility s1. (* Loss feels larger than gain *)
Proof.
  intros.
  (* Example proof steps depend on concrete definitions *)
Admitted.

Definition reciprocity (a1 a2 : Action) : Prop :=
  match a1, a2 with
  | Give, Give => True
  | Take, Take => True
  | _, _ => False
  end.

Lemma reciprocity_invariant :
  forall a1 a2 : Action,
    reciprocity a1 a2 -> reciprocity a2 a1.
Proof.
  intros.
  destruct a1, a2; simpl; auto.
Qed.

Inductive Belief : Type :=
  | BelieveA
  | BelieveB.

Inductive Evidence : Type :=
  | EvidenceA
  | EvidenceB
  | EvidenceNeutral.

Definition confirms (b : Belief) (e : Evidence) : Prop :=
  match b, e with
  | BelieveA, EvidenceA => True
  | BelieveB, EvidenceB => True
  | _, _ => False
  end.

Lemma confirmation_bias :
  forall b : Belief,
    exists e : Evidence, confirms b e.
Proof.
  intros.
  destruct b.
  - exists EvidenceA. simpl. auto.
  - exists EvidenceB. simpl. auto.
Qed.

Lemma combined_invariant :
  forall b : Belief, a : Action,
    (exists e : Evidence, confirms b e) -> reciprocity a a.
Proof.
  intros.
  destruct a; simpl; auto.
Qed.
