import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.gridspec import GridSpec

# Set style parameters
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("deep")
sns.set_context("talk")
plt.rcParams["figure.figsize"] = (14, 8)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.labelsize'] = 18  # Increased to 18 for consistency
plt.rcParams['axes.titlesize'] = 20  # Increased to 20
plt.rcParams['xtick.labelsize'] = 16  # Increased to 16
plt.rcParams['ytick.labelsize'] = 16  # Increased to 16
plt.rcParams['legend.fontsize'] = 16  # Increased to 16
plt.rcParams['figure.titlesize'] = 24  # Increased to 24

# Define model names and colors for consistency
models = ["Courteasy-v1", "DeepSeek-r1", "GPT-4.1", "Llama-3.1-405B"]
model_colors = {
    "Courteasy-v1": "#3182CE",  # blue
    "DeepSeek-r1": "#38A169",   # green
    "GPT-4.1": "#DD6B20",       # orange
    "Llama-3.1-405B": "#805AD5" # purple
}

# Data for the plots
# --------------------------------------

# Figure 1: Model Accuracy Comparison
accuracy_data = {
    'model': ["Courteasy-v1", "DeepSeek-r1", "GPT-4.1", "Llama-3.1-405B"],
    'AIBE-18': [87.0, 81.5, 79.3, 78.3],
    'AIBE-19': [73.1, 77.4, 71.0, 72.0],
    # 'Change': [-13.9, -4.1, -8.3, -6.3]
}
accuracy_df = pd.DataFrame(accuracy_data)

# Figure 2: Correctness Score Distribution (AIBE-18)
correctness_aibe18 = {
    'model': models,
    'Score 5': [81, 73, 73, 68],
    'Score 4': [0, 0, 0, 2],
    'Score 3': [0, 1, 0, 0],
    'Score 2': [1, 3, 0, 9],
    'Score 1': [10, 15, 19, 13],
}
correctness_aibe18_df = pd.DataFrame(correctness_aibe18)

# Figure 3: Correctness Score Distribution (AIBE-19)
correctness_aibe19 = {
    'model': models,
    'Score 5': [69, 69, 67, 65],
    'Score 4': [1, 2, 0, 1],
    'Score 3': [1, 0, 0, 1],
    'Score 2': [2, 1, 1, 9],
    'Score 1': [20, 21, 25, 17],
}
correctness_aibe19_df = pd.DataFrame(correctness_aibe19)

# Figure 4: Similarity Score Distribution (AIBE-18)
similarity_aibe18 = {
    'model': models,
    'Score 5': [72, 64, 74, 34],
    'Score 4': [6, 10, 0, 41],
    'Score 3': [2, 1, 0, 1],
    'Score 2': [6, 10, 0, 4],
    'Score 1': [6, 7, 18, 12],
}
similarity_aibe18_df = pd.DataFrame(similarity_aibe18)

# Figure 5: Similarity Score Distribution (AIBE-19)
similarity_aibe19 = {
    'model': models,
    'Score 5': [47, 61, 68, 32],
    'Score 4': [22, 10, 1, 41],
    'Score 3': [0, 1, 0, 2],
    'Score 2': [12, 3, 1, 7],
    'Score 1': [12, 18, 23, 11],
}
similarity_aibe19_df = pd.DataFrame(similarity_aibe19)

# Figure 6: Error Distribution by Category (AIBE-18)
error_categories_aibe18 = {
    'Category': ['Civil Law', 'Criminal Law', 'Constitutional Law', 'Family Law', 'Contract & Commercial Law', 
                 'Evidence & Procedure', 'Labor Law', 'Administrative Law', 'Tax Law', 'Other Areas'],
    'Courteasy-v1': [3, 1, 1, 2, 1, 1, 0, 0, 0, 3],
    'DeepSeek-r1': [5, 4, 1, 1, 1, 0, 1, 0, 1, 3],
    'GPT-4.1': [5, 3, 1, 3, 2, 1, 2, 1, 0, 1],
    'Llama-3.1-405B': [3, 7, 1, 1, 2, 1, 1, 1, 1, 2]
}
error_categories_aibe18_df = pd.DataFrame(error_categories_aibe18)

# Figure 7: Error Distribution by Category (AIBE-19)
error_categories_aibe19 = {
    'Category': ['Criminal Law', 'Constitutional Law', 'Civil Law', 'Contract & Commercial Law', 
                 'Family Law', 'Labor Law', 'Evidence & Procedure', 'Administrative Law', 'Other Areas'],
    'Courteasy-v1': [5, 5, 3, 4, 2, 1, 0, 1, 4],
    'DeepSeek-r1': [6, 3, 1, 3, 1, 1, 0, 2, 4],
    'GPT-4.1': [6, 4, 5, 4, 1, 1, 1, 0, 5],
    'Llama-3.1-405B': [7, 3, 2, 4, 1, 1, 1, 2, 5]
}
error_categories_aibe19_df = pd.DataFrame(error_categories_aibe19)

# Figure 8: Universal Errors (AIBE-18)
universal_errors_aibe18 = {
    'Category': ['Civil Law', 'Criminal Law', 'Constitutional Law'],
    'Count': [3, 1, 1]
}
universal_errors_aibe18_df = pd.DataFrame(universal_errors_aibe18)

# Figure 9: Universal Errors (AIBE-19)
universal_errors_aibe19 = {
    'Category': ['Contract & Commercial Law', 'Criminal Law', 'Other Areas', 
                'Constitutional Law', 'Family Law', 'Labor Law'],
    'Count': [3, 2, 2, 1, 1, 1]
}
universal_errors_aibe19_df = pd.DataFrame(universal_errors_aibe19)

# Figure 10: Performance on Recent Legislation (AIBE-19)
recent_legislation = {
    'Legislation': ['BNS (Penal Code)', 'BNSS (Procedure)', 'BSA (Evidence)', 'Labor Codes 2020', 'Total'],
    'Questions': [7, 6, 4, 3, 20],
    'Courteasy-v1': [3, 2, 2, 0, 7],
    'DeepSeek-r1': [2, 2, 1, 0, 5],
    'GPT-4.1': [2, 1, 1, 0, 4],
    'Llama-3.1-405B': [1, 1, 1, 0, 3]
}
recent_legislation_df = pd.DataFrame(recent_legislation)

# Function to calculate percentages
def calculate_percentage(row):
    if row['Legislation'] == 'Total':
        return row[2:] / row['Questions'] * 100
    else:
        return row[2:] / row['Questions'] * 100

recent_legislation_percentages = recent_legislation_df.apply(calculate_percentage, axis=1)
recent_legislation_percentages['Legislation'] = recent_legislation_df['Legislation']
recent_legislation_percentages['Questions'] = recent_legislation_df['Questions']

# Create the visualizations
# --------------------------------------

# Function to create and save plots
def create_plots():
    """Create all plots for the report and save them"""
    
    # Figure 1: Model Accuracy Comparison
    plt.figure(figsize=(14, 8))
    x = np.arange(len(accuracy_df['model']))
    width = 0.35
    
    plt.bar(x - width/2, accuracy_df['AIBE-18'], width, label='AIBE-18', color='#3182CE')
    plt.bar(x + width/2, accuracy_df['AIBE-19'], width, label='AIBE-19', color='#E53E3E')
    
    plt.xlabel('Model', fontsize=18)
    plt.ylabel('Accuracy (%)', fontsize=18)
    plt.title('Figure 1: Model Accuracy Comparison', fontsize=20)
    plt.xticks(x, accuracy_df['model'], rotation=0)
    plt.ylim(0, 100)  # Fixed y-axis from 0-100%
    
    # Add accuracy values on top of each bar
    for i, value in enumerate(accuracy_df['AIBE-18']):
        plt.text(i - width/2, value + 0.5, f"{value:.1f}%", ha='center', va='bottom')
    for i, value in enumerate(accuracy_df['AIBE-19']):
        plt.text(i + width/2, value + 0.5, f"{value:.1f}%", ha='center', va='bottom')
    
    # # Add the change value between bars with consistent color
    # for i, value in enumerate(accuracy_df['Change']):
    #     text = f"{value:.1f}%"
    #     plt.text(i, accuracy_df['AIBE-19'][i] + 3, text, ha='center', va='bottom', color='black', fontweight='bold')
    
    plt.legend(fontsize=16, title_fontsize=18)
    plt.tight_layout()
    plt.savefig('figure1_model_accuracy.png', dpi=300, bbox_inches='tight')
    
    # Calculate max y-value for consistent scale in correctness/similarity charts
    correctness_max = max(
        correctness_aibe18_df[['Score 5', 'Score 4', 'Score 3', 'Score 2', 'Score 1']].max().max(),
        correctness_aibe19_df[['Score 5', 'Score 4', 'Score 3', 'Score 2', 'Score 1']].max().max()
    )
    correctness_max = int(correctness_max * 1.1)  # Add 10% margin
    
    similarity_max = max(
        similarity_aibe18_df[['Score 5', 'Score 4', 'Score 3', 'Score 2', 'Score 1']].max().max(),
        similarity_aibe19_df[['Score 5', 'Score 4', 'Score 3', 'Score 2', 'Score 1']].max().max()
    )
    similarity_max = int(similarity_max * 1.1)  # Add 10% margin
    
    # Figure 2a: Correctness Score Distribution (AIBE-18)
    plt.figure(figsize=(14, 10))
    correctness_aibe18_melted = pd.melt(correctness_aibe18_df, id_vars=['model'], 
                                      var_name='Score', value_name='Count')
    ax = sns.barplot(data=correctness_aibe18_melted, x='Score', y='Count', hue='model', 
               palette=model_colors)
    plt.title('Figure 2a: Correctness Score Distribution (AIBE-18)', fontsize=20)
    plt.xlabel('Correctness Score', fontsize=18)
    plt.ylabel('Number of Questions', fontsize=18)
    plt.ylim(0, correctness_max)  # Same y-axis for both
    
    # Add a legend with larger font size
    plt.legend(fontsize=16, title_fontsize=18)
    plt.tight_layout()
    plt.savefig('figure2a_correctness_scores_aibe18.png', dpi=300, bbox_inches='tight')
    
    # Figure 2b: Correctness Score Distribution (AIBE-19)
    plt.figure(figsize=(14, 10))
    correctness_aibe19_melted = pd.melt(correctness_aibe19_df, id_vars=['model'], 
                                      var_name='Score', value_name='Count')
    ax = sns.barplot(data=correctness_aibe19_melted, x='Score', y='Count', hue='model', 
               palette=model_colors)
    plt.title('Figure 2b: Correctness Score Distribution (AIBE-19)', fontsize=20)
    plt.xlabel('Correctness Score', fontsize=18)
    plt.ylabel('Number of Questions', fontsize=18)
    plt.ylim(0, correctness_max)  # Same y-axis for both
    
    # Add a legend with larger font size
    plt.legend(fontsize=16, title_fontsize=18)
    plt.tight_layout()
    plt.savefig('figure2b_correctness_scores_aibe19.png', dpi=300, bbox_inches='tight')
    
    # Figure 3a: Similarity Score Distribution (AIBE-18)
    plt.figure(figsize=(14, 10))
    similarity_aibe18_melted = pd.melt(similarity_aibe18_df, id_vars=['model'], 
                                     var_name='Score', value_name='Count')
    ax = sns.barplot(data=similarity_aibe18_melted, x='Score', y='Count', hue='model', 
               palette=model_colors)
    plt.title('Figure 3a: Similarity Score Distribution (AIBE-18)', fontsize=20)
    plt.xlabel('Similarity Score', fontsize=18)
    plt.ylabel('Number of Questions', fontsize=18)
    plt.ylim(0, similarity_max)  # Same y-axis for both
    
    # Add a legend with larger font size
    plt.legend(fontsize=16, title_fontsize=18)
    plt.tight_layout()
    plt.savefig('figure3a_similarity_scores_aibe18.png', dpi=300, bbox_inches='tight')
    
    # Figure 3b: Similarity Score Distribution (AIBE-19)
    plt.figure(figsize=(14, 10))
    similarity_aibe19_melted = pd.melt(similarity_aibe19_df, id_vars=['model'], 
                                     var_name='Score', value_name='Count')
    ax = sns.barplot(data=similarity_aibe19_melted, x='Score', y='Count', hue='model', 
               palette=model_colors)
    plt.title('Figure 3b: Similarity Score Distribution (AIBE-19)', fontsize=20)
    plt.xlabel('Similarity Score', fontsize=18)
    plt.ylabel('Number of Questions', fontsize=18)
    plt.ylim(0, similarity_max)  # Same y-axis for both
    
    # Add a legend with larger font size
    plt.legend(fontsize=16, title_fontsize=18)
    plt.tight_layout()
    plt.savefig('figure3b_similarity_scores_aibe19.png', dpi=300, bbox_inches='tight')
    
    # Calculate max y-value for consistent error category charts
    error_max = max(
        error_categories_aibe18_df[models].max().max(),
        error_categories_aibe19_df[models].max().max()
    )
    error_max = int(error_max * 1.1)  # Add 10% margin
    
    # Figure 5: Error Distribution by Category (AIBE-18)
    plt.figure(figsize=(18, 10))
    error_categories_aibe18_melted = pd.melt(error_categories_aibe18_df, id_vars=['Category'], 
                                          var_name='Model', value_name='Errors')
    
    # Sort categories by total errors
    category_totals = error_categories_aibe18_melted.groupby('Category')['Errors'].sum().sort_values(ascending=False)
    error_categories_aibe18_melted['Category'] = pd.Categorical(
        error_categories_aibe18_melted['Category'], 
        categories=category_totals.index, 
        ordered=True
    )
    
    sns.barplot(data=error_categories_aibe18_melted, x='Category', y='Errors', hue='Model', palette=model_colors)
    plt.title('Figure 4a: Error Distribution by Legal Category (AIBE-18)', fontsize=20)
    plt.xlabel('Legal Category', fontsize=18)
    plt.ylabel('Number of Errors', fontsize=18)
    plt.ylim(0, error_max)  # Same y-axis scale for both error charts
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Model', fontsize=16, title_fontsize=18)
    plt.tight_layout()
    plt.savefig('figure4a_error_distribution_aibe18.png', dpi=300, bbox_inches='tight')
    
    # Figure 6: Error Distribution by Category (AIBE-19)
    plt.figure(figsize=(18, 10))
    error_categories_aibe19_melted = pd.melt(error_categories_aibe19_df, id_vars=['Category'], 
                                          var_name='Model', value_name='Errors')
    
    # Sort categories by total errors
    category_totals = error_categories_aibe19_melted.groupby('Category')['Errors'].sum().sort_values(ascending=False)
    error_categories_aibe19_melted['Category'] = pd.Categorical(
        error_categories_aibe19_melted['Category'], 
        categories=category_totals.index, 
        ordered=True
    )
    
    sns.barplot(data=error_categories_aibe19_melted, x='Category', y='Errors', hue='Model', palette=model_colors)
    plt.title('Figure 4b: Error Distribution by Legal Category (AIBE-19)', fontsize=20)
    plt.xlabel('Legal Category', fontsize=18)
    plt.ylabel('Number of Errors', fontsize=18)
    plt.ylim(0, error_max)  # Same y-axis scale for both error charts
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Model', fontsize=16, title_fontsize=18)
    plt.tight_layout()
    plt.savefig('figure4b_error_distribution_aibe19.png', dpi=300, bbox_inches='tight')
    
    # Figure 7: Universal Errors Pie Charts (both AIBE exams)
    fig, axes = plt.subplots(1, 2, figsize=(18, 9))
    
    # AIBE-18 Universal Errors
    universal_colors = sns.color_palette('Set3', len(universal_errors_aibe18_df))
    axes[0].pie(universal_errors_aibe18_df['Count'], labels=universal_errors_aibe18_df['Category'], 
                autopct='%1.1f%%', startangle=90, colors=universal_colors)
    axes[0].set_title('Figure 5a: Questions All Models Failed (AIBE-18)')
    axes[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    
    # AIBE-19 Universal Errors
    universal_colors = sns.color_palette('Set3', len(universal_errors_aibe19_df))
    axes[1].pie(universal_errors_aibe19_df['Count'], labels=universal_errors_aibe19_df['Category'], 
                autopct='%1.1f%%', startangle=90, colors=universal_colors)
    axes[1].set_title('Figure 5b: Questions All Models Failed (AIBE-19)')
    axes[1].axis('equal')
    
    plt.tight_layout()
    plt.savefig('figure5_universal_errors.png', dpi=300, bbox_inches='tight')
    
    # Figure 8: Performance on Recent Legislation (AIBE-19)
    plt.figure(figsize=(16, 10))
    
    # Filter out the "Total" row for the main visualization
    legislation_df = recent_legislation_df[recent_legislation_df['Legislation'] != 'Total']
    
    # Extract model columns and melt for plotting
    model_cols = ['Courteasy-v1', 'DeepSeek-r1', 'GPT-4.1', 'Llama-3.1-405B']
    legislation_melted = pd.melt(legislation_df, 
                               id_vars=['Legislation', 'Questions'], 
                               value_vars=model_cols,
                               var_name='Model', value_name='Correct')
    
    # Add a percentage column
    legislation_melted['Percentage'] = (legislation_melted['Correct'] / legislation_melted['Questions']) * 100
    
    # Create the grouped bar chart
    ax = sns.barplot(data=legislation_melted, x='Legislation', y='Percentage', hue='Model', palette=model_colors)
    
    # Add the total questions count above each group
    for i, legis in enumerate(legislation_df['Legislation']):
        plt.text(i, 100, f"n={legislation_df.iloc[i]['Questions']}", ha='center', va='bottom')
    
    # Add value labels on the bars
    for p in ax.patches:
        height = p.get_height()
        if height > 0:  # Only add labels to visible bars
            ax.text(p.get_x() + p.get_width()/2., height + 1,
                    f'{height:.0f}%', ha="center", va='bottom')
    
    plt.title('Figure 6: Performance on Recent Legislation Questions (AIBE-19)', fontsize=20)
    plt.xlabel('Legislation Type', fontsize=18)
    plt.ylabel('Percentage Correct (%)', fontsize=18)
    plt.ylim(0, 110)  # Make room for the labels above the bars
    plt.xticks(rotation=0)  # Keep legislation names horizontal
    plt.legend(title='Model', fontsize=16, title_fontsize=18)
    plt.tight_layout()
    plt.savefig('figure6_recent_legislation.png', dpi=300, bbox_inches='tight')
    
    # Figure 9: Overall Error Count Comparison
    plt.figure(figsize=(14, 8))
    
    # Collect total errors for each model in both exams
    total_errors = {
        'Model': models,
        'AIBE-18': [12, 17, 19, 20],
        'AIBE-19': [25, 21, 27, 26]
    }
    total_errors_df = pd.DataFrame(total_errors)
    total_max = total_errors_df[['AIBE-18', 'AIBE-19']].max().max()
    total_max = int(total_max * 1.1)  # Add 10% margin
    
    total_errors_melted = pd.melt(total_errors_df, id_vars=['Model'], 
                                var_name='Exam', value_name='Errors')
    
    sns.barplot(data=total_errors_melted, x='Model', y='Errors', hue='Exam', 
               palette={'AIBE-18': '#3182CE', 'AIBE-19': '#E53E3E'})
    
    plt.title('Figure 7: Total Error Count by Model', fontsize=20)
    plt.xlabel('Model', fontsize=18)
    plt.ylabel('Number of Errors', fontsize=18)
    plt.ylim(0, total_max)  # Fixed y-axis scale
    
    # Add error count on top of each bar
    for i, p in enumerate(plt.gca().patches):
        height = p.get_height()
        plt.text(p.get_x() + p.get_width()/2., height + 0.5, f"{height}", ha='center', va='bottom')
    
    plt.legend(title='Exam', fontsize=16, title_fontsize=18)
    plt.tight_layout()
    plt.savefig('figure7_total_errors.png', dpi=300, bbox_inches='tight')
    
    # Figure 10: Performance Summary Dashboard
    # This combines key metrics into a single dashboard visual
    fig = plt.figure(figsize=(20, 16))
    gs = GridSpec(3, 2, figure=fig)
    
    # Accuracy comparison
    ax1 = fig.add_subplot(gs[0, :])
    x = np.arange(len(accuracy_df['model']))
    width = 0.35
    
    ax1.bar(x - width/2, accuracy_df['AIBE-18'], width, label='AIBE-18', color='#3182CE')
    ax1.bar(x + width/2, accuracy_df['AIBE-19'], width, label='AIBE-19', color='#E53E3E')
    
    ax1.set_title('Accuracy Comparison (%)')
    ax1.set_xticks(x)
    ax1.set_xticklabels(accuracy_df['model'])
    ax1.set_ylim(0, 100)  # Fixed y-axis from 0-100%
    
    # Add accuracy values on top of each bar
    for i, value in enumerate(accuracy_df['AIBE-18']):
        ax1.text(i - width/2, value + 0.5, f"{value:.1f}%", ha='center', va='bottom')
    for i, value in enumerate(accuracy_df['AIBE-19']):
        ax1.text(i + width/2, value + 0.5, f"{value:.1f}%", ha='center', va='bottom')
    
    # # Add change percentages with black text
    # for i, value in enumerate(accuracy_df['Change']):
    #     text = f"{value:.1f}%"
    #     ax1.text(i, (accuracy_df['AIBE-18'][i] + accuracy_df['AIBE-19'][i])/2, 
    #             text, ha='center', va='center', color='black', fontweight='bold')
    
    ax1.legend()
    
    # Top error categories AIBE-18
    ax2 = fig.add_subplot(gs[1, 0])
    top_categories_18 = error_categories_aibe18_df.set_index('Category').sum(axis=1).nlargest(5).index
    errors_18_top = error_categories_aibe18_df[error_categories_aibe18_df['Category'].isin(top_categories_18)]
    errors_18_melted = pd.melt(errors_18_top, id_vars=['Category'], var_name='Model', value_name='Errors')
    
    sns.barplot(data=errors_18_melted, x='Category', y='Errors', hue='Model', palette=model_colors, ax=ax2)
    ax2.set_title('Top 5 Error Categories (AIBE-18)')
    ax2.set_xlabel('')
    ax2.set_ylabel('Number of Errors')
    ax2.set_ylim(0, error_max)  # Same y-axis scale
    ax2.tick_params(axis='x', rotation=30)
    ax2.legend().remove()  # Remove legend as we'll add a common one
    
    # Top error categories AIBE-19
    ax3 = fig.add_subplot(gs[1, 1])
    top_categories_19 = error_categories_aibe19_df.set_index('Category').sum(axis=1).nlargest(5).index
    errors_19_top = error_categories_aibe19_df[error_categories_aibe19_df['Category'].isin(top_categories_19)]
    errors_19_melted = pd.melt(errors_19_top, id_vars=['Category'], var_name='Model', value_name='Errors')
    
    sns.barplot(data=errors_19_melted, x='Category', y='Errors', hue='Model', palette=model_colors, ax=ax3)
    ax3.set_title('Top 5 Error Categories (AIBE-19)')
    ax3.set_xlabel('')
    ax3.set_ylabel('Number of Errors')
    ax3.set_ylim(0, error_max)  # Same y-axis scale
    ax3.tick_params(axis='x', rotation=30)
    ax3.legend().remove()  # Remove legend as we'll add a common one
    
    # Recent legislation performance
    ax4 = fig.add_subplot(gs[2, :])
    
    # Use the total row for a summary
    total_row = recent_legislation_df[recent_legislation_df['Legislation'] == 'Total']
    total_melted = pd.melt(total_row, id_vars=['Legislation', 'Questions'], 
                         value_vars=models, var_name='Model', value_name='Correct')
    total_melted['Percentage'] = (total_melted['Correct'] / total_melted['Questions']) * 100
    
    sns.barplot(data=total_melted, x='Model', y='Percentage', palette=model_colors, ax=ax4)
    ax4.set_title('Performance on Recent Legislation (AIBE-19)')
    ax4.set_xlabel('')
    ax4.set_ylabel('Percentage Correct (%)')
    ax4.set_ylim(0, 50)  # Reasonable scale for the data
    
    # Add correct/total counts on bars
    for i, row in enumerate(total_melted.itertuples()):
        correct = row.Correct
        total = row.Questions
        ax4.text(i, row.Percentage + 1, f"{correct}/{total} ({row.Percentage:.1f}%)", 
                ha='center', va='bottom')
    
    # Add a common legend for the entire figure
    handles, labels = ax3.get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, 0.02), ncol=4)
    
    plt.suptitle('Figure 8: AI Legal Models Performance Summary', fontsize=22, y=0.98)
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig('figure8_performance_summary.png', dpi=300, bbox_inches='tight')
    
    print("All plots have been created and saved with fixed y-axis scales.")

# Run the function to create all plots
create_plots()