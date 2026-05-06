"""
Model evaluation and metrics module
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve,
)
import numpy as np
import pandas as pd


class ModelEvaluator:
    """Class for evaluating classification models"""
    
    def __init__(self, y_true, y_pred, y_pred_proba=None):
        """Initialize evaluator with predictions"""
        self.y_true = y_true
        self.y_pred = y_pred
        self.y_pred_proba = y_pred_proba
    
    def get_classification_metrics(self):
        """Calculate classification metrics"""
        metrics = {
            'accuracy': accuracy_score(self.y_true, self.y_pred),
            'precision': precision_score(self.y_true, self.y_pred),
            'recall': recall_score(self.y_true, self.y_pred),
            'f1': f1_score(self.y_true, self.y_pred),
        }
        
        # Try to calculate ROC-AUC if probabilities available
        if self.y_pred_proba is not None:
            try:
                metrics['roc_auc'] = roc_auc_score(self.y_true, self.y_pred_proba[:, 1])
            except:
                pass
        
        return metrics
    
    def print_metrics(self):
        """Print all evaluation metrics"""
        metrics = self.get_classification_metrics()
        
        print("\n" + "="*50)
        print("EVALUATION METRICS")
        print("="*50)
        print(f"Accuracy:  {metrics['accuracy']:.4f}")
        print(f"Precision: {metrics['precision']:.4f}")
        print(f"Recall:    {metrics['recall']:.4f}")
        print(f"F1-Score:  {metrics['f1']:.4f}")
        if 'roc_auc' in metrics:
            print(f"ROC-AUC:   {metrics['roc_auc']:.4f}")
    
    def get_confusion_matrix(self):
        """Get confusion matrix"""
        cm = confusion_matrix(self.y_true, self.y_pred)
        return cm
    
    def print_confusion_matrix(self):
        """Print confusion matrix details"""
        cm = self.get_confusion_matrix()
        
        print("\n" + "="*50)
        print("CONFUSION MATRIX")
        print("="*50)
        print("Predicted:    0    1")
        print(f"Actual 0:  {cm[0][0]:4d} {cm[0][1]:4d}")
        print(f"Actual 1:  {cm[1][0]:4d} {cm[1][1]:4d}")
        
        # Calculate and print derived metrics
        tn, fp, fn, tp = cm[0][0], cm[0][1], cm[1][0], cm[1][1]
        specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
        sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
        
        print(f"\nSensitivity (True Positive Rate): {sensitivity:.4f}")
        print(f"Specificity (True Negative Rate): {specificity:.4f}")
    
    def get_classification_report(self):
        """Get detailed classification report"""
        report = classification_report(
            self.y_true, self.y_pred,
            target_names=['Not Placed', 'Placed'],
            output_dict=False
        )
        return report
    
    def print_classification_report(self):
        """Print detailed classification report"""
        print("\n" + "="*50)
        print("CLASSIFICATION REPORT")
        print("="*50)
        print(self.get_classification_report())
    
    def print_all_evaluations(self):
        """Print all evaluation reports"""
        self.print_metrics()
        self.print_confusion_matrix()
        self.print_classification_report()


def evaluate_model(model, X_test, y_test):
    """Convenience function to evaluate a trained model"""
    y_pred = model.predict(X_test)
    
    try:
        y_pred_proba = model.predict_proba(X_test)
    except:
        y_pred_proba = None
    
    evaluator = ModelEvaluator(y_test, y_pred, y_pred_proba)
    return evaluator


if __name__ == "__main__":
    print("Evaluation module loaded successfully")
